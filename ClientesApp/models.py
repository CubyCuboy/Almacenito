from django.db import models
from gestionApp.models import Producto

class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=50)
    ap_cliente = models.CharField(max_length=50)
    am_cliente = models.CharField(max_length=50)
    rut_cliente = models.CharField(max_length=12, primary_key=True) 
    direccion_cliente = models.CharField(max_length=80)
    numero_dir_cliente = models.CharField(max_length=10) 
    fono_cliente = models.CharField(max_length=15) 
    estado = models.CharField(
        max_length=30,
        choices=[
            ('Sin pagos pendientes', 'Sin pagos pendientes'),
            ('Por crédito por pagar', 'Por crédito por pagar'),
            ('Crédito atrasado', 'Crédito atrasado'),
            ('Crédito pagado', 'Crédito pagado'),
        ],
        default='Sin pagos pendientes',
    )
    productos_adeudados = models.ManyToManyField(Producto, blank=True)
    fecha_pago = models.DateField(null=True, blank=True)  

    def __str__(self):
        return f"{self.nombre_cliente} {self.ap_cliente} - {self.rut_cliente}"
