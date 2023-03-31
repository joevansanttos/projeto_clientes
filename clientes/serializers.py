from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "O CPF deve ter 11 digitos!!"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "Nao inclua numeros nesse nome"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError("O Rg deve ter 9 digitos")
        return data

    # def validate_celular(self, celular):
    #     if len(celular) < 11:
    #         raise serializers.ValidationError("O celular deve ter 11 dígitos")
    #     return celular








