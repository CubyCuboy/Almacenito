from django import forms
from gestionApp.models import Producto, Proveedor, Categoria
import re

class RegistroProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['codigo_proveedor', 'razon_social_proveedor', 'empresa', 'fono', 'correo', 'direccion']

    razon_social_proveedor = forms.CharField(
        label="Razón Social",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    empresa = forms.CharField(
        label="Empresa",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    fono = forms.IntegerField(
        label="Teléfono",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    correo = forms.EmailField(
        label="Correo Electrónico",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    direccion = forms.CharField(
        label="Dirección",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    def clean_razon_social_proveedor(self):
        razon_social = self.cleaned_data['razon_social_proveedor'].strip()
        # Verificar si el proveedor ya existe, pero no si estamos editando el mismo proveedor
        if not self.instance.pk and Proveedor.objects.filter(razon_social_proveedor=razon_social).exists():
            raise forms.ValidationError("Ya existe un proveedor con esta razón social.")
        return razon_social

    def clean_correo(self):
        input_email = self.cleaned_data['correo'].strip()
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", input_email):
            raise forms.ValidationError("Debe ingresar un correo válido.")
        # Verificar si el correo ya existe, pero no si estamos editando el mismo proveedor
        if not self.instance.pk and Proveedor.objects.filter(correo=input_email).exists():
            raise forms.ValidationError("El correo electrónico ya está en uso.")
        return input_email

class RegistroProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'descripcion', 'stock', 'categoria', 'proveedor', 'precio']

    nombre_producto = forms.CharField(
        label="Nombre Producto",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    descripcion = forms.CharField(
        label="Descripción",
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    stock = forms.IntegerField(
        label="Stock",
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        min_value=0 
    )
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        label="Categoría",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    proveedor = forms.ModelChoiceField(
        queryset=Proveedor.objects.all(),
        label="Proveedor",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    precio = forms.IntegerField(
        label="Precio",
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        min_value=0 
    )

    def clean_nombre_producto(self):
        nombre_producto = self.cleaned_data['nombre_producto'].strip()
        # Verificar si el producto ya existe, pero no si estamos editando el mismo producto
        if not self.instance.pk and Producto.objects.filter(nombre_producto=nombre_producto).exists():
            raise forms.ValidationError("Ya existe un producto con este nombre.")
        return nombre_producto

class RegistroCategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre_categoria', 'descripcion_categoria']

    nombre_categoria = forms.CharField(
        label="Nombre Categoría",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    descripcion_categoria = forms.CharField(
        label="Descripción",
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

    def clean_nombre_categoria(self):
        nombre_categoria = self.cleaned_data['nombre_categoria'].strip()
        if not self.instance.pk and Categoria.objects.filter(nombre_categoria=nombre_categoria).exists():
            raise forms.ValidationError("Ya existe una categoría con este nombre.")
        return nombre_categoria
