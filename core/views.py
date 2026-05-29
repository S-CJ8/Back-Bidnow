from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import filters, viewsets

from .models import MetodoPago, Producto, Puja, Subasta, Transaccion, Usuario
from .serializers import (
    MetodoPagoSerializer,
    ProductoSerializer,
    PujaSerializer,
    SubastaSerializer,
    TransaccionSerializer,
    UsuarioSerializer,
)


@extend_schema_view(
    list=extend_schema(summary="Listar usuarios", tags=["Usuario"]),
    retrieve=extend_schema(summary="Obtener usuario", tags=["Usuario"]),
    create=extend_schema(summary="Crear usuario", tags=["Usuario"]),
    update=extend_schema(summary="Actualizar usuario (PUT)", tags=["Usuario"]),
    partial_update=extend_schema(
        summary="Actualizar usuario (PATCH)", tags=["Usuario"]
    ),
    destroy=extend_schema(summary="Eliminar usuario", tags=["Usuario"]),
)
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["correo", "nombre"]


@extend_schema_view(
    list=extend_schema(summary="Listar métodos de pago", tags=["Método de pago"]),
    retrieve=extend_schema(summary="Obtener método de pago", tags=["Método de pago"]),
    create=extend_schema(summary="Crear método de pago", tags=["Método de pago"]),
    update=extend_schema(
        summary="Actualizar método de pago (PUT)", tags=["Método de pago"]
    ),
    partial_update=extend_schema(
        summary="Actualizar método de pago (PATCH)", tags=["Método de pago"]
    ),
    destroy=extend_schema(summary="Eliminar método de pago", tags=["Método de pago"]),
)
class MetodoPagoViewSet(viewsets.ModelViewSet):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodoPagoSerializer


@extend_schema_view(
    list=extend_schema(summary="Listar productos", tags=["Producto"]),
    retrieve=extend_schema(summary="Obtener producto", tags=["Producto"]),
    create=extend_schema(summary="Crear producto", tags=["Producto"]),
    update=extend_schema(summary="Actualizar producto (PUT)", tags=["Producto"]),
    partial_update=extend_schema(
        summary="Actualizar producto (PATCH)", tags=["Producto"]
    ),
    destroy=extend_schema(summary="Eliminar producto", tags=["Producto"]),
)
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


@extend_schema_view(
    list=extend_schema(summary="Listar subastas", tags=["Subasta"]),
    retrieve=extend_schema(summary="Obtener subasta", tags=["Subasta"]),
    create=extend_schema(summary="Crear subasta", tags=["Subasta"]),
    update=extend_schema(summary="Actualizar subasta (PUT)", tags=["Subasta"]),
    partial_update=extend_schema(
        summary="Actualizar subasta (PATCH)", tags=["Subasta"]
    ),
    destroy=extend_schema(summary="Eliminar subasta", tags=["Subasta"]),
)
class SubastaViewSet(viewsets.ModelViewSet):
    queryset = Subasta.objects.all()
    serializer_class = SubastaSerializer


@extend_schema_view(
    list=extend_schema(summary="Listar pujas", tags=["Puja"]),
    retrieve=extend_schema(summary="Obtener puja", tags=["Puja"]),
    create=extend_schema(summary="Crear puja", tags=["Puja"]),
    update=extend_schema(summary="Actualizar puja (PUT)", tags=["Puja"]),
    partial_update=extend_schema(summary="Actualizar puja (PATCH)", tags=["Puja"]),
    destroy=extend_schema(summary="Eliminar puja", tags=["Puja"]),
)
class PujaViewSet(viewsets.ModelViewSet):
    queryset = Puja.objects.all()
    serializer_class = PujaSerializer


@extend_schema_view(
    list=extend_schema(summary="Listar transacciones", tags=["Transacción"]),
    retrieve=extend_schema(summary="Obtener transacción", tags=["Transacción"]),
    create=extend_schema(summary="Crear transacción", tags=["Transacción"]),
    update=extend_schema(
        summary="Actualizar transacción (PUT)", tags=["Transacción"]
    ),
    partial_update=extend_schema(
        summary="Actualizar transacción (PATCH)", tags=["Transacción"]
    ),
    destroy=extend_schema(summary="Eliminar transacción", tags=["Transacción"]),
)
class TransaccionViewSet(viewsets.ModelViewSet):
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer
