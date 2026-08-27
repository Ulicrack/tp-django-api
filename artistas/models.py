from django.db import models


class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_artistico = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    edad = models.IntegerField()
    ciudad = models.CharField(max_length=100)
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_artistico


class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    fecha = models.DateField()
    lugar = models.CharField(max_length=100)
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)
    artista = models.ForeignKey(
        Artista,
        on_delete=models.CASCADE,
        related_name="eventos"
    )

    def __str__(self):
        return self.nombre