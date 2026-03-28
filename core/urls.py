from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    MetodoPagoViewSet,
    ProductoViewSet,
    PujaViewSet,
    SubastaViewSet,
    TransaccionViewSet,
    UsuarioViewSet,
)

router = DefaultRouter()
router.register(r"usuarios", UsuarioViewSet, basename="usuario")
router.register(r"metodos-pago", MetodoPagoViewSet, basename="metodopago")
router.register(r"productos", ProductoViewSet, basename="producto")
router.register(r"subastas", SubastaViewSet, basename="subasta")
router.register(r"pujas", PujaViewSet, basename="puja")
router.register(r"transacciones", TransaccionViewSet, basename="transaccion")

urlpatterns = [
    path("", include(router.urls)),
]
