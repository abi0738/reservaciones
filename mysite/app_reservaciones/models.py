from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Habitacion(models.Model):
    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=50)
    precio_noche = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, default='Disponible')

    def __str__(self):
        return f'Habitación {self.numero}'

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()

    def __str__(self):
        return f'Reserva de {self.cliente} en Habitación {self.habitacion.numero}'

class Pago(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()
    metodo_pago = models.CharField(max_length=50)

    def __str__(self):
        return f'Pago de {self.monto} para {self.reserva}'

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_contratacion = models.DateField()

    def __str__(self):
        return self.nombre