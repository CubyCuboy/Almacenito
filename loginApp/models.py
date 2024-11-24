from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, rut, password=None, fono=None, rol=None, **extra_fields):
        if not rut:
            raise ValueError("El campo RUT es obligatorio.")

        if rol != 'Admin' and not fono:
            raise ValueError("El campo teléfono es obligatorio para usuarios no administradores.")

        is_admin = rol == 'Admin'
        extra_fields.setdefault('is_staff', is_admin)
        extra_fields.setdefault('is_superuser', is_admin)

        user = self.model(rut=rut, fono=fono, rol=rol, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, rut, password=None, fono=None, **extra_fields):
        return self.create_user(rut, password, fono=fono, rol='Admin', **extra_fields)

class usuario(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=50)
    ap_p = models.CharField(max_length=50)
    ap_m = models.CharField(max_length=50)
    fono = models.BigIntegerField(null=True, blank=True)
    email = models.EmailField(max_length=250)
    rut = models.CharField(max_length=12, primary_key=True)
    rol = models.CharField(
        max_length=12,
        choices=[('Admin', 'Admin'), ('Gerente', 'Gerente'), ('Cajero', 'Cajero')],
        default='Cajero',
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'rut'
    REQUIRED_FIELDS = ['nombre', 'email']

    def __str__(self):
        return f"{self.nombre} ({self.rol})"

    @property
    def can_manage_stock(self):
        return self.rol in ['Admin', 'Gerente']

    @property
    def can_manage_users(self):
        return self.rol == 'Admin'
