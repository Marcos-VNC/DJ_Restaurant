from rest_framework import serializers
from .models import Lanche, Pedido, Ingrediente


class LancheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lanche
        fields = (
            'id',
            'nome',
            'valor',
            'tipo',
            'imagem',
        )


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = (
            'id',
            'nomeCliente',
            'data',
            'fk_Lanche',
            'quantidade',
        )
