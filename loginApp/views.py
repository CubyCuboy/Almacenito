from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from loginApp.models import usuario
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
import re
from django.http import JsonResponse


def validar_rut(rut):
    """Valida un RUT chileno."""
  
    if not re.match(r'^\d{1,8}[\dkK]$', rut):
        return False
    cuerpo, dv = rut[:-1], rut[-1]  
    s = 0
    for i, v in enumerate(reversed(cuerpo)):
        s += int(v) * (i % 6 + 2)
    dv_calculado = 11 - (s % 11)
    if dv_calculado == 11:
        dv_calculado = '0'
    elif dv_calculado == 10:
        dv_calculado = 'K'
    return dv_calculado == dv.upper()


def validar_rut_view(request):
    rut = request.GET.get('rut', '').strip()
    es_valido = validar_rut(rut)
    return JsonResponse({'valid': es_valido})

def registroView(request):
    form = forms.registroForms()
    if request.method == 'POST':
        form = forms.registroForms(request.POST)
        if form.is_valid():
            hashed_password = make_password(form.cleaned_data['password'])
            user = usuario(
                nombre=form.cleaned_data['nombre'],
                ap_p=form.cleaned_data['ap_p'],
                ap_m=form.cleaned_data['ap_m'],
                fono=form.cleaned_data['fono'],
                email=form.cleaned_data['email'],
                rut=form.cleaned_data['rut'],  
                rol=form.cleaned_data['rol'],
                password=hashed_password
            )
            user.save()
            messages.success(request, "Registro completado exitosamente")
            return redirect('login')  
        else:
            messages.error(request, "Error en el formulario, verifica los datos ingresados")
    
    data = {'form': form}
    return render(request, 'register.html', data)




def loginView(request):
    form = forms.loginForms()

    if request.method == 'POST':
        rut = request.POST.get('rut').strip().replace('-', '').replace('.', '')  
        password = request.POST.get('password')


        if not rut or not password:
            messages.error(request, "Por favor, complete todos los campos.")
            return render(request, 'login.html', {'form': form})

        try:
            user = usuario.objects.get(rut=rut)


            if check_password(password, user.password):
                login(request, user)
                messages.success(request, "Inicio de sesión exitoso.")
                return redirect('index')
            else:
                messages.error(request, "Contraseña incorrecta.")

        except usuario.DoesNotExist:
            messages.error(request, "Usuario no encontrado.")

    return render(request, 'login.html', {'form': form})



@login_required
def index(request):
    return render(request, 'main.html')

def exit_view(request):
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente")
    return redirect('login')
