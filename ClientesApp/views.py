from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Cliente
from .forms import ClienteForm, ClienteEstadoForm, ClienteModificarForm, ClienteEliminarForm,ClientePagoForm
from gestionApp.models import Producto
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

# Views de cliente
def ListarClienteView(request):
    search_query = request.GET.get('search', '')  
    estado_filter = request.GET.get('estado', '')
    clientes = Cliente.objects.all()
    if search_query:
        clientes = clientes.filter(nombre_cliente__icontains=search_query)
    if estado_filter:
        clientes = clientes.filter(estado=estado_filter)
    estados_disponibles = Cliente.objects.values_list('estado', flat=True).distinct()

    data = {
        'clientes': clientes,
        'usuario': request.user,
        'search_query': search_query,
        'estado_filter': estado_filter,
        'estados_disponibles': estados_disponibles,
    }
    return render(request, 'listar_clientes.html', data)


@user_passes_test(is_admin_or_gerente)
def CrearClienteView(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente creado exitosamente.")
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'crear_cliente.html', {'form': form})

@user_passes_test(is_admin_or_gerente)
def ActualizarEstadoClienteView(request, rut_cliente):
    cliente = get_object_or_404(Cliente, rut_cliente=rut_cliente)
    if request.method == 'POST':
        form = ClienteEstadoForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes') 
    else:
        form = ClienteEstadoForm(instance=cliente)
    return render(request, 'actualizar_estado.html', {'form': form})

@user_passes_test(is_admin_or_gerente)
def ModificarClienteView(request, rut_cliente):
    cliente = get_object_or_404(Cliente, rut_cliente=rut_cliente)
    tiene_deuda = cliente.productos_adeudados.exists()

    if request.method == 'POST':
        form = ClienteModificarForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            if not tiene_deuda:
                cliente.save()
                return redirect('detalles_cliente', rut_cliente=cliente.rut_cliente)
            else:
                form.add_error('estado', 'No puedes cambiar el estado mientras tengas deuda.')
    else:
        form = ClienteModificarForm(instance=cliente)

    return render(request, 'modificar_cliente.html', {
        'form': form,
        'cliente': cliente,
    })


@user_passes_test(is_admin_or_gerente)
def EliminarClienteView(request, rut_cliente):
    cliente = get_object_or_404(Cliente, rut_cliente=rut_cliente)
    if request.method == 'POST':
        form = ClienteEliminarForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirmacion']:
            cliente.delete()
            messages.success(request, "Cliente eliminado exitosamente.")
            return redirect('listar_clientes')
    else:
        form = ClienteEliminarForm()
    return render(request, 'eliminar_cliente.html', {'form': form})

@user_passes_test(is_admin_or_gerente)
def PagarProductosView(request, rut_cliente):
    cliente = get_object_or_404(Cliente, rut_cliente=rut_cliente)

    if request.method == 'POST':
        form = ClientePagoForm(request.POST, cliente=cliente)
        if form.is_valid():
            productos_a_pagar = form.cleaned_data['productos_a_pagar']
            cliente.productos_adeudados.remove(*productos_a_pagar)

            # Actualizar estado si no hay productos adeudados
            if not cliente.productos_adeudados.exists():
                cliente.estado = 'Crédito pagado'
                cliente.fecha_pago = form.cleaned_data['fecha_pago']
            cliente.save()

            messages.success(request, "El pago se ha registrado exitosamente.")
            return redirect('Listar_clientes')
    else:
        form = ClientePagoForm(cliente=cliente)

    return render(request, 'pagar_productos.html', {'form': form, 'cliente': cliente})

def DetallesClienteView(request, rut_cliente):
    cliente = get_object_or_404(Cliente, rut_cliente=rut_cliente)
    productos_adeudados = cliente.productos_adeudados.all()  
    valor_total = sum(producto.precio for producto in productos_adeudados)  
    context = {
        'cliente': cliente,
        'productos_adeudados': productos_adeudados,
        'valor_total': valor_total,
    }
    return render(request, 'detalles_cliente.html', context)