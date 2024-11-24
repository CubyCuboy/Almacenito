from django import forms
from .models import Cliente
from gestionApp.models import Producto
from django.core.exceptions import ValidationError
import re
from django.utils import timezone
from django.utils.timezone import now 


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre_cliente', 'ap_cliente', 'am_cliente', 'rut_cliente',
            'direccion_cliente', 'numero_dir_cliente', 'fono_cliente',
            'estado', 'fecha_pago'
        ]
        widgets = {
            'nombre_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del cliente'}),
            'ap_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido paterno'}),
            'am_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido materno'}),
            'rut_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RUT'}),
            'direccion_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'numero_dir_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número'}),
            'fono_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'fecha_pago': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean_rut_cliente(self):
        rut = self.cleaned_data['rut_cliente']
        # Verificar que el RUT tenga un formato válido
        rut_pattern = r'^\d{7,8}-[0-9kK]$'  # Formato RUT Chileno
        if not re.match(rut_pattern, rut):
            raise ValidationError("El RUT ingresado no tiene un formato válido.")
        return rut


class ClienteEstadoForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['estado', 'fecha_pago']

        widgets = {
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'fecha_pago': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean_estado(self):
        estado = self.cleaned_data['estado']
        if estado == 'Crédito pagado':
            self.instance.productos_adeudados.clear()
            if not self.cleaned_data['fecha_pago']:
                self.cleaned_data['fecha_pago'] = timezone.now()
        return estado


class ClienteModificarForm(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ['estado', 'productos_adeudados', 'fecha_pago']

        widgets = {
            'nombre_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del cliente'}),
            'ap_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido paterno'}),
            'am_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido materno'}),
            'rut_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RUT'}),
            'direccion_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'numero_dir_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número'}),
            'fono_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
        }


class ClienteEliminarForm(forms.Form):
    confirmacion = forms.BooleanField(
        label="¿Estás seguro de que deseas eliminar este cliente?",
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )



class ClientePagoForm(forms.ModelForm):
    productos_a_pagar = forms.ModelMultipleChoiceField(
        queryset=Producto.objects.none(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        required=False,
        label="Selecciona los productos a pagar",
    )
    pagar_todo = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label="Marcar para pagar todos los productos adeudados",
    )

    class Meta:
        model = Cliente
        fields = ['productos_a_pagar', 'pagar_todo', 'fecha_pago']
        widgets = {
            'fecha_pago': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        cliente = kwargs.pop('cliente', None)
        super().__init__(*args, **kwargs)
        if cliente:
            self.fields['productos_a_pagar'].queryset = cliente.productos_adeudados.all()
    def clean(self):
        cleaned_data = super().clean()  
        pagar_todo = cleaned_data.get('pagar_todo')
        productos_a_pagar = cleaned_data.get('productos_a_pagar')
        if not pagar_todo and not productos_a_pagar:
            raise forms.ValidationError("Debes seleccionar al menos un producto o marcar la opción de pagar todo.")
        if pagar_todo:
            cleaned_data['productos_a_pagar'] = self.fields['productos_a_pagar'].queryset
        if not cleaned_data.get('fecha_pago'):
            cleaned_data['fecha_pago'] = now()
        return cleaned_data