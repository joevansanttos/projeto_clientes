from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"Número de CPF inválido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Não inclua números neste campo"})
        if not rg_valido(data['rg']):
<<<<<<< HEAD
            raise serializers.ValidationError({'rg': "O Rg deve ter 9 digitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': "O celular deve ter o seguinte formato 71 99783-8747"})
        return data

    


=======
            raise serializers.ValidationError({'rg':"O RG deve ter 9 dígitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O número de celular deve seguir este modelo: 11 91234-1234 (respeitando os espaços e traço)"})
        return data

>>>>>>> 524d4ba (adding new validatords)






