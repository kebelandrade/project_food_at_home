from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import *
import datetime
from .validaciones import *


# willaism daniel santos
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, error_messages={
        'blank': 'No puede ir en blanco el nombre.',
        'max_length': 'El Nombre no puede ir más 40 caracteres.',
        'null': 'Por favor, proporcione un nombre.'
    })
    apellidos = models.CharField(max_length=40, error_messages={
        'blank': 'No puede ir en blanco el nombre.',
        'max_length': 'No puede ir más 40 caracteres.',
        'null': 'Por favor, proporcione un nombre.'
    })
    nombreUsuario = models.CharField(max_length=15, unique=True, error_messages={
        'blank': 'El Nombre de Usuario no puede ir en blanco.',
        'max_length': 'El Nombre de Usuario no puede ir más 15 caracteres.',
        'null': 'Por favor, proporcione un Nombre de Usuario.',
        'unique': 'El Nombre de Usuario ya existe.'
    })
    password = models.CharField(max_length=20, error_messages={
        'blank': 'La contraseña no puede ir en blanco.',
        'null': 'Por favor, proporcione una contraseña.',
        'max_length': 'La contraseña no puede ser mayor de 20 caracteres'
    })
    telefono = models.CharField(max_length=8, error_messages={
        'blank': 'No puede ir en blanco el Teléfono.',
        'max_length': 'El número de teléfono no puede llevar más de 8 dígitos.',
        'null': 'Por favor, proporcione un número de teléfono.'
    })
    email = models.EmailField(validators=[
        EmailValidator("El correo es inválido.")
    ])
    tipoUsuario = models.IntegerField(validators=[
        MinValueValidator(2, "El valor debe ser mayor a 2."),
        MaxValueValidator(3, "El valor máximo es de 3.")
    ], default='SOME STRING', error_messages={
        'blank': 'No puede ir en blanco el Teléfono.',
        'null': 'Por favor, proporcione un número de teléfono.'
    })


class DireccionUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=25, error_messages={
        'blank': 'No puede ir en blanco el nombre.',
        'max_length': 'No puede ir más 25 caracteres.',
        'null': 'Por favor, proporcione un nombre.'
    }, validators=[validar_alfa])
    ciudad = models.ForeignKey('Ciudad', on_delete=models.PROTECT)
    direccion = models.CharField(max_length=150, error_messages={
        'blank': 'La dirección no puede ir en blanco.',
        'max_length': 'No puede ir más 150 caracteres.',
        'null': 'Por favor, proporcione una dirección.'
    })
    latitud = models.FloatField()
    longitud = models.FloatField()


class Transporte(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, error_messages={
        'blank': 'No puede ir en blanco el nombre.',
        'max_length': 'No puede ir más 20 caracteres.',
        'null': 'Por favor, proporcione un nombre.'
    })


class Restaurante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, error_messages={
        'blank': 'No puede ir en blanco el nombre.',
        'max_length': 'No puede ir más 50 caracteres.',
        'null': 'Por favor, proporcione un nombre.'
    })
    telefono = models.CharField(max_length=8, error_messages={
        'blank': 'No puede ir en blanco el número de teléfono.',
        'max_length': 'El número de teléfono no puede ser más de 8 dígitos.',
        'null': 'Por favor, proporcione un número de teléfono.'
    }, validators=[validar_telefono])
    estado = models.BooleanField(default=True)
    calificacion = models.IntegerField(validators=[
        MinValueValidator(1, "El valor debe ser mayor a 1."),
        MaxValueValidator(5, "El valor máximo es de 5.")
    ])
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)


class Ciudad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, error_messages={
        'blank': 'No puede ir en blanco el nombre.',
        'max_length': 'No puede ir más 30 caracteres.',
        'null': 'Por favor, proporcione un nombre.'
    }, validators=[validar_alfa])


class DireccionRestaurante(models.Model):
    id = models.AutoField(primary_key=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.PROTECT)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT)
    ubicacion = models.CharField(max_length=150, error_messages={
        'blank': 'No puede ir en blanco la ubicación.',
        'max_length': 'No puede ir más 150 caracteres.',
        'null': 'Por favor, proporcione una ubicación.'
    })
    latitud = models.FloatField()
    longitud = models.FloatField()
    estado = models.BooleanField()


class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    identidad = models.CharField(max_length=13, unique=True, error_messages={
        'blank': 'No puede ir en blanco la identidad.',
        'null': 'Por favor, proporcione una identidad.',
        'unique': 'La identida ya está en uso.'
    }, validators=[validar_telefono])
    nombre_completo = models.CharField(max_length=50, error_messages={
        'blank': 'No puede ir en blanco el nombre completo.',
        'max_length': 'El Nombre completo no puede ir más 50 letras.',
        'null': 'Por favor, proporcione un nombre.'
    }, validators=[validar_alfa])
    usuario = models.CharField(max_length=15, unique=True, error_messages={
        'blank': 'No puede ir en blanco el campo usuario.',
        'max_length': 'El usuario no puede llevar más 15 caracteres.',
        'null': 'Por favor, proporcione un usuario.',
        'unique': 'El usuario ya existe.'
    })
    password = models.CharField(max_length=20 , error_messages={
        'blank': 'No puede ir en blanco la contraseña.',
        'null': 'Por favor, proporcione una contraseña.',
        'max_length': 'La contraseña no puede ser mayor de 20 caracteres'
    })
    telefono = models.CharField(max_length=8, error_messages={
        'blank': 'No puede ir en blanco el número de teléfono.',
        'max_length': 'El número de teléfono no puede ser más de 8 dígitos.',
        'null': 'Por favor, proporcione un número de teléfono.'
    }, validators=[validar_telefono])

    def clean(self):
        if not len(self.identidad) == 13:
            raise ValidationError("La identidad debe ser de 13 dígitos")
    estado = models.BooleanField()


class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    transporte = models.ForeignKey(Transporte, on_delete=models.PROTECT)
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    fecha_pedido = models.DateTimeField()
    direccion = models.ForeignKey(DireccionUsuario, on_delete=models.PROTECT)
    calificacion = models.IntegerField(validators=[
        MinValueValidator(1, "El valor debe ser mayor a 1."),
        MaxValueValidator(5, "El valor máximo es de 5.")
    ])
    precioPedido = models.DecimalField(max_digits=6,decimal_places=2, validators=[
        MinValueValidator(0.01, message="El precio no puede ser menor a cero")
    ])

    def clean(self):
        if self.fecha_pedido.timestamp() <= datetime.datetime.now().timestamp():
            raise ValidationError("La fecha del pedido debe ser mayor a la actual.")


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, error_messages={
        'blank': 'No puede ir en blanco el nombre.',
        'max_length': 'No puede ir más 20 caracteres.',
        'null': 'Por favor, proporcione un nombre.'
    }, validators=[validar_alfa])
<<<<<<< HEAD
    
=======
    img = models.CharField(max_length=250, default="")
    descripcion = models.CharField(max_length=40, default="")
>>>>>>> ec6574d18aab3735a26726a4dd1ddddad5d42221


class Plato(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, error_messages={
        'blank': 'No puede ir en blanco el nombre.',
        'max_length': 'No puede ir más 20 caracteres.',
        'null': 'Por favor, proporcione un nombre.'
    })
    descripcion = models.CharField(max_length=250, error_messages={
        'max_length': 'No puede usar más de 250 caracteres en la descripción.',
        'null': 'Por favor, proporcione una descripción del plato.',
        'blank': 'No dejar vacío el campo de descripción.'
    })
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    precio = models.DecimalField(max_digits=6, decimal_places=2, validators=[
        MinValueValidator(0.01, message="El precio no puede ser menor a cero")
    ])
    img = models.FileField(max_length=100)


class BodyPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    plato = models.ForeignKey(Plato, on_delete=models.PROTECT)
    cantidad = models.IntegerField(error_messages={
        'blank': 'No puede dejar vacío el campo de cantidad.',
        'null': 'Por favor, proporcione una cantidad.'
    })
    precio = models.DecimalField(max_digits=6, decimal_places=2, validators=[
        MinValueValidator(0.01, message="El precio no puede ser menor a cero")
    ])


class CalificacionRestaurante(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.PROTECT)
    calificacion = models.IntegerField(validators=[
        MinValueValidator(1, "El valor debe ser mayor a 1."),
        MaxValueValidator(5, "El valor máximo es de 5.")
    ])
    observacion = models.CharField(max_length=250, error_messages={
        'max_length': 'La observación no puede llevar más de 250 caracteres.'
    })


class BitacoraEmpleado(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    precio = models.DecimalField(max_digits=6, decimal_places=2, validators=[
        MinValueValidator(0.01, message="El precio no puede ser menor a cero")
    ])


class Promocion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
