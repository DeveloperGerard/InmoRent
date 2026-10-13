from django.db import models

# Create your models here.

class Comuna(models.Model):
    nombre = models.CharField(max_length=100,unique=True)
    region = models.CharField(max_length=100)
    activa = models.BooleanField(default=True)
    codigo_clasificacion = models.CharField(max_length=10,unique=True)

    def  __str__(self):
        return f"{self.nombre}. {self.codigo_clasificacion}"


class Propiedad(models.Model):
    codigo_propiedad =  models.CharField(max_length=10, unique=True) 
    direccion =  models.CharField(max_length=200) 
    tipo_propiedad= models.CharField(choices=[ ("DEPARTAMENTO","DEPARTAMENTO"), ("CASA","CASA"), ("OFICINA","OFICINA")]) 
    precio_arriendo = models.IntegerField() 
    dormitorios=  models.IntegerField() 
    banos= models.IntegerField() 
    disponible = models.BooleanField(default=True) 
    fecha_publicacion =models.DateField(auto_now_add=True) 
    comuna =  models.ForeignKey(Comuna, on_delete=models.CASCADE, related_name='propiedades') 




