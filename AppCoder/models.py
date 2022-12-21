from django.db import models

# Create your models here.
class Adopcion(models.Model):
    nombre_de_Mascota=models.CharField(max_length=40)
    edad=models.FloatField()
    genero = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    castracion = models.CharField(max_length=40)
    nombre_del_Tutelar=models.CharField(max_length=40)
    telefono=models.IntegerField()
    mail= models.EmailField(max_length=200, blank=True, null=True)

class Provisorios(models.Model):
    nombreProvisorio=models.CharField(max_length=40)
    tipo=models.CharField(max_length=40)
    genero= models.CharField(max_length=40)
    animalesenCasa=models.CharField(max_length=40)
    telefono=models.IntegerField()
    mail= models.EmailField(max_length=200, blank=True, null=True)

class Encontrados(models.Model):
    nombreRetiene=models.CharField(max_length=40)
    telefono=models.IntegerField()
    mail= models.EmailField(max_length=200, blank=True, null=True)