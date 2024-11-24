import re
from django import forms
from loginApp.models import usuario

class registroForms(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ['nombre', 'ap_p', 'ap_m', 'fono', 'email', 'rut', 'rol', 'password']  

    ROLES = [('Admin', 'ADMIN'), ('Gerente', 'GERENTE'), ('Cajero', 'CAJERO')]
    
    nombre = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control'}))
    ap_p = forms.CharField(label="Apellido paterno", widget=forms.TextInput(attrs={'class': 'form-control'}))
    ap_m = forms.CharField(label="Apellido Materno", widget=forms.TextInput(attrs={'class': 'form-control'}))
    fono = forms.IntegerField(label="Teléfono", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Correo electrónico", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    rut = forms.CharField(label="RUT", widget=forms.TextInput(attrs={'class': 'form-control'}))
    rol = forms.ChoiceField(choices=ROLES, label="Rol", widget=forms.Select(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Contraseña")

    def clean_email(self):
        inputEmail = self.cleaned_data['email'].strip()
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", inputEmail):
            raise forms.ValidationError("Debe ingresar un correo válido.")
        
        # Comprobar si el email ya existe
        if usuario.objects.filter(email=inputEmail).exists():
            raise forms.ValidationError("El correo electrónico ya está en uso.")
        
        return inputEmail

    def clean_password(self):
        inputPassword = self.cleaned_data['password']
        if len(inputPassword) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not any(char.isupper() for char in inputPassword):
            raise forms.ValidationError("La contraseña debe contener al menos una letra mayúscula.")
        if not any(char.isdigit() for char in inputPassword):
            raise forms.ValidationError("La contraseña debe contener al menos un número.")
        return inputPassword

    def clean_rut(self):
        rut = self.cleaned_data['rut'].strip().replace('-', '').replace('.', '')  # Limpiar RUT
        if not self.validar_rut(rut):  
            raise forms.ValidationError("El RUT ingresado no es válido.")
        
        return rut

    @staticmethod
    def validar_rut(rut):
        """Valida un RUT chileno."""
        if not re.match(r'^\d{1,8}[\dkK]$', rut):
            return False
        
        cuerpo, dv = rut[:-1], rut[-1].upper() 

        s = 0
        for i, v in enumerate(reversed(cuerpo)):
            s += int(v) * (i % 6 + 2)

        dv_calculado = 11 - (s % 11)
        if dv_calculado == 11:
            dv_calculado = '0'
        elif dv_calculado == 10:
            dv_calculado = 'K'

        return str(dv_calculado) == dv

class loginForms(forms.Form):
    rut = forms.CharField(max_length=12, required=True, label="RUT", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True, label="Contraseña")

    def clean_rut(self):
        rut = self.cleaned_data['rut'].strip().replace('-', '').replace('.', '')  
        if not registroForms.validar_rut(rut):  
            raise forms.ValidationError("El RUT ingresado no es válido.")
        
        return rut
