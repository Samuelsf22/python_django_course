from django.db import models
import datetime  # permite poder usar el DateField()

# Create your models here.

class Docente(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    especialidad = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


STATUS_CHOICES = (
    ('I', 'Implementación'),
    ('R', 'Revisión'),
    ('E', 'Error'),
    ('A', 'Aprobados')
)

class Lista_curso(models.Model):
    creacion = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField()
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre} - {self.docente}'


class WebDocente(models.Model):
    nombre = models.CharField(max_length=60)
    url_fb = models.URLField(unique=True)
    descripcion = models.TextField()
    fecha_creacion = models.DateField()
    ranking = models.IntegerField()
    estado = models.CharField(choices=STATUS_CHOICES, max_length=1)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre} - {self.docente}'