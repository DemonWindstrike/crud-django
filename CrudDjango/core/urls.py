from django.urls import path
from requests import delete
from .views import anya, listado_Manga, agregar_Producto, editar_Producto, delete_producto

urlpatterns = [
    path('', anya , name="anya"),
    path('agregarProducto/', agregar_Producto, name="agregarProductos"),
    path('listadoProductos/', listado_Manga , name="listadoProductos"),
    path('editarProducto/<pk>', editar_Producto, name="editarProductos"),
    path('deleteProducto/<pk>', delete_producto, name="deleteProductos"),

]
