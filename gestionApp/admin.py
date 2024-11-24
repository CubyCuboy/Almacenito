from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from .models import Producto, Proveedor, Categoria

# Decorador para restringir acceso a usuarios específicos
def admin_or_manager_required(view_func):
    @method_decorator(login_required)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_superuser or request.user.rol in ['Admin', 'Gerente']:
            return view_func(request, *args, **kwargs)
        return redirect('no_permiso')
    return _wrapped_view

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('codigo_proveedor', 'razon_social_proveedor', 'empresa', 'fono', 'correo', 'direccion')
    search_fields = ('codigo_proveedor', 'razon_social_proveedor', 'empresa')
    list_filter = ('empresa',)
    ordering = ('codigo_proveedor',)

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.rol == 'Admin'

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.rol == 'Admin'

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('codigo_categoria', 'nombre_categoria')
    search_fields = ('codigo_categoria', 'nombre_categoria')
    ordering = ('codigo_categoria',)

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.rol == 'Admin'

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.rol == 'Admin'

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo_producto', 'nombre_producto', 'categoria', 'proveedor', 'precio', 'stock')
    search_fields = ('codigo_producto', 'nombre_producto')
    list_filter = ('categoria', 'proveedor')
    ordering = ('codigo_producto',)

    def has_change_permission(self, request, obj=None):
        # Permitir solo si el usuario es superuser, admin o gerente
        return request.user.is_superuser or request.user.rol in ['Admin', 'Gerente']

    def has_delete_permission(self, request, obj=None):
        # Permitir eliminar solo a superuser o admin
        return request.user.is_superuser or request.user.rol == 'Admin'

    def has_add_permission(self, request):
        # Los cajeros no pueden agregar productos
        return request.user.is_superuser or request.user.rol in ['Admin', 'Gerente']
