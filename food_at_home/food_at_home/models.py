from django.db import models


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    nombre_usuario = models.CharField(max_length=15, unique=True)
    telefono = models.CharField(max_length=8)
    email = models.EmailField()


class DireccionUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=25)
    direccion = models.CharField(max_length=150)


class Transporte(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)


class Restaurante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=8)
    estado = models.BooleanField(default=True)
    calificacion = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)


class Ciudad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)


class DireccionRestaurante(models.Model):
    id = models.AutoField(primary_key=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.PROTECT)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT)
    ubicacion = models.CharField(max_length=150)


class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    identidad = models.CharField(max_length=13, unique=True)
    nombre_completo = models.CharField(max_length=50)
    usuario = models.CharField(max_length=15)
    telefono = models.CharField(max_length=8)


class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    transporte = models.ForeignKey(Transporte, on_delete=models.PROTECT)
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    fecha_pedido = models.DateTimeField()
    direccion = models.ForeignKey(DireccionUsuario, on_delete=models.PROTECT)


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)


class Plato(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=250)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    precio = models.DecimalField(max_digits=6, decimal_places=2)


class BodyPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    plato = models.ForeignKey(Plato, on_delete=models.PROTECT)
    cantidad = models.IntegerField()


class CalificacionPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    calificacion = models.IntegerField()
    observacion = models.CharField(max_length=250)


class CalificacionRestaurante(models.Model):
    id_pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    calificacion = models.IntegerField()
    Observacion = models.CharField(max_length=250)


class BitacoraEmpleado(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
