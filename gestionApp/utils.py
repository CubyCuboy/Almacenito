from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test

def verificar_rol_permitido(*roles_permitidos):
    """
    Decorador para verificar si el usuario tiene un rol permitido.
    """
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if hasattr(request.user, 'rol') and request.user.rol in roles_permitidos:
                return view_func(request, *args, **kwargs)
            return redirect('no_permiso')
        return _wrapped_view
    return decorator

# Decoradores específicos
def admin_o_gerente(view_func):
    return verificar_rol_permitido('Admin', 'Gerente')(view_func)

def todos(view_func):
    return verificar_rol_permitido('Cajero', 'Admin', 'Gerente')(view_func)
