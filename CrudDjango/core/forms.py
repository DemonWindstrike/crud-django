from django import forms
from django.forms import ModelForm
from .models import productos

#crear la clase formularioproductos

class productosForm(ModelForm):
    
    class Meta :
        model = productos
        fields = ['nombreProducto', 'categoria', 'descripcion', 'imagen']