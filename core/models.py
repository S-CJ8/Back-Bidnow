from django.db import models


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    correo = models.CharField(max_length=100, unique=True)
    contrasena = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "usuario"

    def __str__(self):
        return self.correo or str(self.id_usuario)


class MetodoPago(models.Model):
    id_metodo_pago = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    numero_referencia = models.CharField(max_length=100, blank=True, null=True)
    titular = models.CharField(max_length=100, blank=True, null=True)
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        db_column="id_usuario",
        related_name="metodos_pago",
    )

    class Meta:
        db_table = "metodo_pago"


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.TextField(blank=True, null=True)
    precio_inicial = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    estado = models.CharField(max_length=50, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    vendedor = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        db_column="id_vendedor",
        related_name="productos",
    )

    class Meta:
        db_table = "producto"


class Subasta(models.Model):
    id_subasta = models.AutoField(primary_key=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    producto = models.OneToOneField(
        Producto,
        on_delete=models.CASCADE,
        db_column="id_producto",
        related_name="subasta",
    )
    subastador = models.ForeignKey(
        Usuario,
        on_delete=models.DO_NOTHING,
        db_column="id_subastador",
        related_name="subastas",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "subasta"


class Puja(models.Model):
    id_puja = models.AutoField(primary_key=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    subasta = models.ForeignKey(
        Subasta,
        on_delete=models.CASCADE,
        db_column="id_subasta",
        related_name="pujas",
    )
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.DO_NOTHING,
        db_column="id_usuario",
        related_name="pujas",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "puja"


class Transaccion(models.Model):
    subasta = models.ForeignKey(
        Subasta, on_delete=models.SET_NULL, null=True, blank=True
    )
    usuario = models.ForeignKey(
        Usuario, on_delete=models.SET_NULL, null=True, blank=True
    )
    monto_final = models.DecimalField(
        max_digits=14, decimal_places=2, null=True, blank=True
    )
    estado = models.CharField(max_length=50, blank=True, default="completada")
    nombre_destinatario = models.CharField(max_length=200, blank=True)
    direccion_envio = models.TextField(blank=True)
    ciudad = models.CharField(max_length=100, blank=True)
    pais = models.CharField(max_length=100, blank=True)
    codigo_postal = models.CharField(max_length=20, blank=True)
    numero_seguimiento = models.CharField(max_length=100, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "transaccion"
