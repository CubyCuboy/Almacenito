from django.db import models
from django.db.models import Max

class Categoria(models.Model):
    codigo_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100)
    descripcion_categoria = models.CharField(max_length=250,null=True)
    def save(self, *args, **kwargs):
        if self.codigo_categoria is None:
            max_codigo = Categoria.objects.aggregate(Max('codigo_categoria'))['codigo_categoria__max'] or 10199
            self.codigo_categoria = max_codigo + 1 if max_codigo < 10299 else None
        super(Categoria, self).save(*args, **kwargs)
    def __str__(self):
        return self.nombre_categoria

class Proveedor(models.Model):
    codigo_proveedor = models.AutoField(primary_key=True)
    razon_social_proveedor = models.CharField(max_length=50)
    empresa = models.CharField(max_length=100)
    fono = models.BigIntegerField()
    correo = models.EmailField(max_length=50)
    direccion = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if self.codigo_proveedor is None:
            max_codigo = Proveedor.objects.aggregate(models.Max('codigo_proveedor'))['codigo_proveedor__max'] or 10100
            self.codigo_proveedor = max_codigo + 1 if max_codigo < 10199 else None
        super(Proveedor, self).save(*args, **kwargs)

    def __str__(self):
        return self.razon_social_proveedor


class Producto(models.Model):
    codigo_producto = models.CharField(max_length=5, primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.TextField()
    stock = models.IntegerField()
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.codigo_producto:
            last_producto = Producto.objects.all().order_by('-codigo_producto').first()  
            if last_producto:
                try:
                    last_code = int(last_producto.codigo_producto)
                    new_code = f"{last_code + 1:05d}"  
                except ValueError:
                    raise ValueError("El formato del código_producto no es válido para autoincrementar.")
            else:
                new_code = "10001"  
            self.codigo_producto = new_code
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.codigo_producto} - {self.nombre_producto}"

