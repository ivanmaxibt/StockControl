from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.IntegerField()

    def __str__(self):
        return self.nombre + " " + self.apellido


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.FloatField()
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
