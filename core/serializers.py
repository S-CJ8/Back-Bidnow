from rest_framework import serializers

from .models import MetodoPago, Producto, Puja, Subasta, Transaccion, Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"


class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = "__all__"


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"


class SubastaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subasta
        fields = "__all__"


class PujaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puja
        fields = "__all__"


class TransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields = "__all__"
