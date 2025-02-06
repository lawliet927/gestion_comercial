from django.db import models

class Edificacion(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Tienda(models.Model):
    nombre = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)
    edificacion = models.ForeignKey(Edificacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Propietario(models.Model):
    nombre_completo = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    foto = models.ImageField(upload_to='propietarios_fotos/')

    def __str__(self):
        return self.nombre_completo


class FechaEntrega(models.Model):
    fecha = models.DateField()
    proyecto = models.ForeignKey(Edificacion, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.proyecto.nombre} - {self.fecha}'

