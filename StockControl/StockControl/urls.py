from django.urls import path
from compra.views import home, agregar_proveedor, agregar_producto, listar_productos

urlpatterns = [
    path('', home, name='home'),
    path('agregar_proveedor/', agregar_proveedor, name='agregar_proveedor'),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
    path('listar_productos/', listar_productos, name='listar_productos'),
]