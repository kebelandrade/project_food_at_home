from django.db import models
from django.core.exceptions import ValidationError


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, error_messages={
        'blank': 'No puede ir en blanco el nombre.',
        'max_length': 'El Nombre no puede ir más 40 letras.',
        'null': 'Por favor, proporcione un nombre.'
    })
    apellidos = models.CharField(max_length=40, error_messages={
        'blank': 'No puede ir en blanco el nombre.',
        'max_length': 'No puede ir más 40 letras.',
        'null': 'Por favor, proporcione un nombre.'
    })
    nombreUsuario = models.CharField(max_length=15, unique=True, error_messages={
        'blank': 'El Nombre de Usuario no puede ir en blanco.',
        'max_length': 'El Nombre de Usuario no puede ir más 15 letras.',
        'null': 'Por favor, proporcione un Nombre de Usuario.',
        'unique': 'El Nombre de Usuario ya existe.'
    })
    password = models.CharField(error_messages={
        'blank': 'La contraseña no puede ir en blanco.',
        'null': 'Por favor, proporcione una contraseña.'
    })
    telefono = models.CharField(max_length=8, error_messages={
        'blank': 'No puede ir en blanco el Teléfono.',
        'max_length': 'El número de teléfono no puede llevar más de 8 dígitos.',
        'null': 'Por favor, proporcione un número de teléfono.'
    })
    email = models.EmailField(error_messages={
        'invalid': 'El correo está inválido.'
    })

    def clean(self):
        if not self.nombre.isalpha() & self.apellidos.isalpha():
            raise ValidationError("El nombre y apellido solo debe contener datos alfabeticos.")

        if not self.telefono.isnumeric():
            raise ValidationError("El número de teléfono solo debe contener números.")


class DireccionUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    usario = models.ForeignKey('Usuario', on_delete=models.PROTECT)
    nombre = models.CharField(max_length=25, error_messages={
        'blank': 'No puede ir en blanco el nombre.',
        'max_length': 'No puede ir más 25 letras.',
        'null': 'Por favor, proporcione un nombre.'
    })
    ciudad = models.ForeignKey('Ciudad', on_delete=models.PROTECT)
    direccion = models.CharField(max_length=150, error_messages={
        'blank': 'La dirección no puede ir en blanco.',
        'max_length': 'No puede ir más 150 letras.',
        'null': 'Por favor, proporcione una dirección.'
    })
    latitud = models.FloatField()
    longitud = models.FloatField()


class Transporte(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, error_messages={
        'blank': 'No puede ir en blanco el nombre.',
        'max_length': 'No puede ir más 20 letras.',
        'null': 'Por favor, proporcione un nombre.'
    })


class Restaurante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, error_messages={
        'blank': 'No puede ir en blanco el nombre.',
        'max_length': 'No puede ir más 50 letras.',
        'null': 'Por favor, proporcione un nombre.'
    })
    telefono = models.CharField(max_length=8, error_messages={
        'blank': 'No puede ir en blanco el número de teléfono.',
        'max_length': 'El número de teléfono no puede ser más de 8 dígitos.',
        'null': 'Por favor, proporcione un número de teléfono.'
    })
    estado = models.BooleanField(default=True)
    calificacion = models.CharField(error_messages={
        'blank': 'No puede ir en blanco la clasificación.',
        'null': 'Por favor, proporcione una clasificación.'
    })
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

    def clean(self):
        if not self.telefono.isnumeric():
            raise ValidationError("El número de teléfono solo puede contener números.")


class Ciudad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, error_messages={
        'blank': 'No puede ir en blanco el nombre.',
        'max_length': 'No puede ir más 30 letras.',
        'null': 'Por favor, proporcione un nombre.'
    })

    def clean(self):
        if not self.nombre.isalpha():
            raise ValidationError("El nombre de la ciudad solo debe contener datos alfanumericos.")


class DireccionRestaurante(models.Model):
    id = models.AutoField(primary_key=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.PROTECT)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT)
    ubicacion = models.CharField(max_length=150)
    latitud = models.FloatField()
    longitud = models.FloatField()


class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    identidad = models.CharField(max_length=13, unique=True)
    nombre_completo = models.CharField(max_length=50)
    usuario = models.CharField(max_length=15, unique=True)
    password = models.CharField()
    telefono = models.CharField(max_length=8)


class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    transporte = models.ForeignKey(Transporte, on_delete=models.PROTECT)
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    fecha_pedido = models.DateTimeField()
    direccion = models.ForeignKey(DireccionUsuario, on_delete=models.PROTECT)
    calificacion = models.IntegerField()
    precioPedido = models.DecimalField(max_digits=6,decimal_places=2)


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)


class Plato(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=250)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    img = models.CharField(max_length=100)


class BodyPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    plato = models.ForeignKey(Plato, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)


class CalificacionRestaurante(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.PROTECT)
    calificacion = models.IntegerField()
    observacion = models.CharField(max_length=250)


class BitacoraEmpleado(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    precio = models.DecimalField(max_digits=6, decimal_places=2)

