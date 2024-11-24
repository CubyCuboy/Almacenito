from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from gestionApp.models import Producto, Proveedor, Categoria
from gestionApp.forms import RegistroProductoForm, RegistroProveedorForm, RegistroCategoriaForm
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import logout


# Permisos
def is_admin_or_gerente(user):
    return user.is_superuser or user.rol in ['Admin', 'Gerente']

def no_permiso(request):
    previous_url = request.META.get('HTTP_REFERER', None)
    context = {
        "mensaje": "No tienes permiso para acceder a esta página.",
        "previous_url": previous_url,
    }
    return render(request, 'no_permiso.html', context)

# Función de borrado universal
def eliminar_objeto(request, modelo, id_objeto, nombre_objeto, url_redireccion, campo_id):
    try:
        objeto = get_object_or_404(modelo, **{campo_id: id_objeto})
        objeto.delete()
        messages.success(request, f"{nombre_objeto} eliminado correctamente.")
    except ObjectDoesNotExist:
        messages.error(request, f"No se pudo encontrar el {nombre_objeto} con ID {id_objeto}.")
    return redirect(url_redireccion)


# Views de productos
def busquedaStockView(request):
    query = request.GET.get('query', '')
    codigo = request.GET.get('codigo', '')
    proveedor_id = request.GET.get('proveedor', '')
    categoria_id = request.GET.get('categoria', '')
    productos = Producto.objects.all()
    
    if query:
        productos = productos.filter(nombre_producto__icontains=query) | productos.filter(descripcion__icontains=query)
    if codigo:
        productos = productos.filter(codigo_producto=codigo)
    if proveedor_id:
        productos = productos.filter(proveedor__codigo_proveedor=proveedor_id)
    if categoria_id:
        productos = productos.filter(categoria__codigo_categoria=categoria_id)
    proveedores = Proveedor.objects.all()
    categorias = Categoria.objects.all()
    data = {
        'productos': productos,
        'query': query,
        'codigo': codigo,
        'proveedor_id': proveedor_id,
        'categoria_id': categoria_id,
        'proveedores': proveedores,
        'categorias': categorias,
        'usuario': request.user
    }

    return render(request, 'busqueda_stock.html', data)


def autocompletar_nombre_producto(request):
    query = request.GET.get('query', '').strip()
    if query:
        nombres = Producto.objects.filter(nombre_producto__icontains=query).values_list('nombre_producto', flat=True)[:10]
        return JsonResponse(list(nombres), safe=False)
    return JsonResponse([], safe=False)

@user_passes_test(is_admin_or_gerente)
def agregarStockView(request):
    if request.method == 'POST':
        form = RegistroProductoForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, "Producto agregado correctamente.")
            return redirect('busq_stock')
    else:
        form = RegistroProductoForm()

    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()

    context = {
        'form': form,
        'categorias': categorias,
        'proveedores': proveedores,
        'titulo': 'Agregar Producto',
        'url_regresar': 'busq_stock',
    }
    return render(request, 'agregar.html', context)

@user_passes_test(is_admin_or_gerente)
def gestionStockView(request, codigo_producto):
    codigo_producto = f"{int(codigo_producto):05d}"
    try:
        producto = get_object_or_404(Producto, codigo_producto=codigo_producto)
    except Producto.DoesNotExist:
        messages.error(request, f"El producto con código {codigo_producto} no existe.")
        return redirect('busq_stock')

    if request.method == 'POST':
        form = RegistroProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save() 
            messages.success(request, "Producto actualizado correctamente.")
            return redirect('busq_stock')
        else:
            messages.error(request, "Hubo un error al actualizar el producto. Verifica los datos ingresados.")
    else:
        form = RegistroProductoForm(instance=producto)

    context = {
        'form': form,
        'titulo': 'Editar Producto',
        'url_regresar': 'busq_stock',  
    }
    return render(request, 'editar.html', context)

@user_passes_test(is_admin_or_gerente)
def eliminar_producto(request, codigo_producto):
    return eliminar_objeto(request, Producto, codigo_producto, "Producto", 'busq_stock', 'codigo_producto')


# Views de proveedores
def busquedaProveedoresView(request):
    query = request.GET.get('query', '')
    proveedores = Proveedor.objects.all()

    if query:
        proveedores = proveedores.filter(razon_social_proveedor__icontains=query)

    data = {
        'proveedores': proveedores,
        'query': query,
    }
    return render(request, 'busqueda_proveedor.html', data)

def autocompletar_nombre_proveedor(request):
    query = request.GET.get('query', '')
    if query:
        proveedores = Proveedor.objects.filter(razon_social_proveedor__icontains=query).values('razon_social_proveedor')[:10]
        nombres = list(proveedor['razon_social_proveedor'] for proveedor in proveedores)
    else:
        nombres = []
    return JsonResponse(nombres, safe=False)

@user_passes_test(is_admin_or_gerente)
def agregarProveedorView(request):
    if request.method == 'POST':
        form = RegistroProveedorForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, "Proveedor agregado correctamente.")
            return redirect('busq_prov')  
    else:
        form = RegistroProveedorForm()

    proveedores = Proveedor.objects.all()

    context = {
        'form': form,
        'proveedores': proveedores,
        'titulo': 'Agregar Proveedor',
        'url_regresar': 'busq_prov',  
    }
    return render(request, 'agregar.html', context)

@user_passes_test(is_admin_or_gerente)
def gestionProveedoresView(request, codigo_proveedor):
    proveedor = get_object_or_404(Proveedor, codigo_proveedor=codigo_proveedor)

    if request.method == 'POST':
        form = RegistroProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()  
            messages.success(request, "Proveedor actualizado correctamente.")
            return redirect('busq_prov')
        else:
            messages.error(request, "Hubo un error al actualizar al editar el proveedor. Verifica los datos ingresados.")
    else:
        form = RegistroProveedorForm(instance=proveedor)

    context = {
        'form': form,
        'titulo': 'Editar Proveedor',  
        'url_regresar': 'busq_prov',  
    }
    return render(request, 'editar.html', context)

@user_passes_test(is_admin_or_gerente)
def eliminarProveedorView(request, codigo_proveedor):
    return eliminar_objeto(request, Proveedor, codigo_proveedor, "Proveedor", 'busq_prov', 'codigo_proveedor')


# Views de categorias
def busquedaCategoriaView(request):
    query = request.GET.get('query', '')
    categorias = Categoria.objects.all()

    if query:
        categorias = categorias.filter(nombre_categoria__icontains=query)

    data = {
        'categorias': categorias,
        'query': query,
    }
    return render(request, 'busqueda_categoria.html', data)

def autocompletar_nombre_categoria(request):
    query = request.GET.get('query', '')
    if query:
        categorias = Categoria.objects.filter(nombre_categoria__icontains=query).values('nombre_categoria')[:10]
        nombres = list(categoria['nombre_categoria'] for categoria in categorias)
    else:
        nombres = []
    return JsonResponse(nombres, safe=False)

@user_passes_test(is_admin_or_gerente)
def agregarCategoriaView(request):
    if request.method == 'POST':
        form = RegistroCategoriaForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, "Categoría agregada correctamente.")
            return redirect('busq_cat')
    else:
        form = RegistroCategoriaForm()

    categorias = Categoria.objects.all()

    context = {
        'form': form,
        'categorias': categorias,
        'titulo': 'Agregar Categoría',
        'url_regresar': 'busq_cat',
    }
    return render(request, 'agregar.html', context)

@user_passes_test(is_admin_or_gerente)
def gestionCategoriaView(request, codigo_categoria=None):
    categoria = None
    if codigo_categoria:
        categoria = get_object_or_404(Categoria, codigo_categoria=codigo_categoria)

    if request.method == 'POST':
        form = RegistroCategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoría guardada correctamente.")
            return redirect('busq_cat')
        else:
            messages.error(request, "Error de validación en el formulario.")
    else:
        form = RegistroCategoriaForm(instance=categoria)

    context = {
        'form': form,
        'titulo': 'Editar Categoría', 
        'url_regresar': 'busq_cat',  
    }
    return render(request, 'editar.html', context)

@user_passes_test(is_admin_or_gerente)
def eliminarCategoriaView(request, codigo_categoria):
    return eliminar_objeto(request, Categoria, codigo_categoria, "Categoría", 'busq_cat', 'codigo_categoria')

