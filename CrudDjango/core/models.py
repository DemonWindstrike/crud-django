from distutils.command.upload import upload
from pickle import TRUE
from unicodedata import category
from django.db import models
from django.forms import IntegerField

# Create your models here.

class productos (models.Model):
    id = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    descripcion = models.TextField(verbose_name='descripcion',null=True)
    imagen = models.ImageField(upload_to='static/core/img', verbose_name='imagen' ,null=True, blank= True)
    precio =models.IntegerField()
    
    def __str__(self): 
        return self.nombreProducto

    def delete(self, using=None, keep_parents=False):
        return super().delete(using, keep_parents)