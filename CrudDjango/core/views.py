from django.shortcuts import render, redirect
from .models import productos
from .forms import productosForm

# Create your views here.

def anya (request):
    return render (request, 'core/anya.html')


def listado_Manga (request):
    mangas = productos.objects.all()

    datos = {'mangas': mangas}
    
    return render(request, 'core/listadoProductos.html', datos)


def agregar_Producto(request):
    if request.method == 'POST':
        formulario = productosForm(request.POST)
        if  formulario.is_valid:
            formulario.save()
            
            return redirect(to="listadoProductos")
    else:
        datos = {'form': productosForm()}        
        return render(request, 'core/agregarProducto.html', datos)    


def editar_Producto (request, pk):
    manga = productos.objects.get(nombreProducto=pk)

    if request.method == 'POST':
        formulario_edit = productosForm(data=request.POST, instance=manga)
        if formulario_edit.is_valid:
            formulario_edit.save()
            
            return redirect(to="listadoProductos")

    else:
        datos = {
        'form':productosForm(instance=manga)
    }
        return render (request, 'core/editarProducto.html', datos)


def delete_producto(request,pk):
    manga = productos.objects.get(nombreProducto=pk)
    manga.delete()
    return redirect(to="listadoProductos")


