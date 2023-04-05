import re
<<<<<<< HEAD

def cpf_valido(numero_do_cpf):
    return len(numero_do_cpf) == 11
=======
from validate_docbr import CPF

def cpf_valido(numero_do_cpf):
    cpf = CPF()
    return cpf.validate(numero_do_cpf)
>>>>>>> 524d4ba (adding new validatords)

def nome_valido(nome):
    return nome.isalpha()

def rg_valido(numero_do_rg):
    return len(numero_do_rg) == 9

def celular_valido(numero_celular):
<<<<<<< HEAD
    """Verifica se o celular é valido"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_celular)
    return resposta
        
=======
    """Verifica se o  celular é valido (11 91234-1234)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_celular)
    return resposta
>>>>>>> 524d4ba (adding new validatords)
