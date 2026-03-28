from django.contrib import admin

from .models import MetodoPago, Producto, Puja, Subasta, Transaccion, Usuario


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id_usuario", "correo", "nombre", "fecha_registro")
    search_fields = ("correo", "nombre")
    ordering = ("-id_usuario",)


@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ("id_metodo_pago", "tipo", "titular", "usuario")
    list_filter = ("tipo",)
    search_fields = ("titular", "numero_referencia")
    ordering = ("-id_metodo_pago",)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id_producto", "titulo", "precio_inicial", "estado", "vendedor")
    list_filter = ("estado",)
    search_fields = ("titulo", "descripcion")
    ordering = ("-id_producto",)


@admin.register(Subasta)
class SubastaAdmin(admin.ModelAdmin):
    list_display = ("id_subasta", "estado", "fecha_inicio", "fecha_fin", "producto", "subastador")
    list_filter = ("estado",)
    ordering = ("-id_subasta",)


@admin.register(Puja)
class PujaAdmin(admin.ModelAdmin):
    list_display = ("id_puja", "monto", "fecha", "subasta", "usuario")
    ordering = ("-id_puja",)


@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ("id_transaccion", "monto_final", "fecha", "subasta", "ganador")
    ordering = ("-id_transaccion",)
