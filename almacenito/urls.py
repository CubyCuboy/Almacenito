from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from loginApp import views as loginApp_views  
from gestionApp.views import (
    busquedaStockView, 
    busquedaProveedoresView, 
    gestionStockView, 
    autocompletar_nombre_producto,
    autocompletar_nombre_proveedor,
    autocompletar_nombre_categoria,
    gestionProveedoresView,
    busquedaCategoriaView,
    gestionCategoriaView,
    eliminar_producto,
    eliminarProveedorView,
    eliminarCategoriaView,
    agregarStockView,
    agregarProveedorView,
    agregarCategoriaView,
    no_permiso,
)
from gestionApp.utils import admin_o_gerente,todos
from ClientesApp.views import(
    ListarClienteView,
    ModificarClienteView,
    ActualizarEstadoClienteView,
    EliminarClienteView,
    CrearClienteView,
    PagarProductosView,
    DetallesClienteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginApp_views.loginView, name='login'),  
    path('registro/', loginApp_views.registroView, name='registro'),
    path('index/', login_required(loginApp_views.index), name='index'),
    path('cuentas/login/', loginApp_views.loginView, name='login_c'),  
    path('cuentas/', include('django.contrib.auth.urls')),  
    path('logout/', loginApp_views.exit_view, name='exit'),

    # Búsquedas (Cajero, Admin y Gerente)
    path('busq_stock/', todos(busquedaStockView), name='busq_stock'),
    path('busq_prov/',todos(busquedaProveedoresView), name='busq_prov'),
    path('busq_cat/',todos(busquedaCategoriaView), name='busq_cat'),

    # Auto completado (Cajero, Admin y Gerente)
    path('autocompletar_nombre_producto/',todos(autocompletar_nombre_producto), name='autocompletar_nombre_producto'),
    path('autocompletar_nombre_proveedor/', todos(autocompletar_nombre_proveedor), name='autocompletar_nombre_proveedor'),
    path('autocompletar_nombre_categoria/', todos(autocompletar_nombre_categoria), name='autocompletar_nombre_categoria'),

    # Gestión (Modificar, solo Admin o Gerente)
    path('crud_stock/<int:codigo_producto>/', admin_o_gerente(gestionStockView), name='crud_stock'),
    path('crud_prov/<int:codigo_proveedor>/', admin_o_gerente(gestionProveedoresView), name='crud_prov'),
    path('crud_cat/<int:codigo_categoria>/', admin_o_gerente(gestionCategoriaView), name='crud_cat'),

    # Gestión (Eliminar, solo Admin o Gerente)
    path('eliminar_producto/<str:codigo_producto>/',admin_o_gerente(eliminar_producto), name='eliminar_producto'),
    path('eliminar_proveedor/<int:codigo_proveedor>/', admin_o_gerente(eliminarProveedorView), name='eliminar_proveedor'),
    path('eliminar_categoria/<int:codigo_categoria>/', admin_o_gerente(eliminarCategoriaView), name='eliminar_categoria'),

    # Gestión (Agregar, solo Admin o Gerente)
    path('agr_stock/', admin_o_gerente(agregarStockView), name='agregar_stock'),
    path('agr_prov/', admin_o_gerente(agregarProveedorView), name='agregar_proveedor'),
    path('agr_cate/', admin_o_gerente(agregarCategoriaView), name='agregar_categoria'),

    # Restricción
    path('no_permiso/',no_permiso, name='no_permiso'),

    # Clientes
    path('listar_clientes',ListarClienteView,name='listar_clientes'),
    path('crear_cliente',admin_o_gerente(CrearClienteView),name='crear_cliente'),
    path('modificar_cliente/<str:rut_cliente>/',admin_o_gerente(ModificarClienteView),name='modificar_cliente'),
    path('actualizar_estado/<str:rut_cliente>',admin_o_gerente(ActualizarEstadoClienteView),name='actualizar_estado'),
    path('eliminar_cliente/<str:rut_cliente>',admin_o_gerente(EliminarClienteView), name='eliminar_cliente'),
    path('detalles_cliente/<str:rut_cliente>',admin_o_gerente(DetallesClienteView), name='detalles_cliente'),
    path('pagar_productos/<str:rut_cliente>',admin_o_gerente(PagarProductosView), name='pagar_productos'),
]
