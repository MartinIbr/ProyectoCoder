from django.db import models

# Create your models here.
class curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()
    def __str__(self):
        return f"{self.nombre} - {self.comision}"

class estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

class profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()
