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
            raise serializers.ValidationError({'rg': "O Rg deve ter 9 digitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': "O celular deve ter o seguinte formato 71 99783-8747"})
        return data

    








