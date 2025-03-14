from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=255)
    edad = models.IntegerField()
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre