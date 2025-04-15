import re
from validate_docbr import CPF

def invalid_cpf(numero_cpf):
    cpf = CPF()
    cpf_valido = cpf.validate(numero_cpf)
    return not cpf_valido

def invalid_nome(nome):
    return not nome.isalpha()

def invalid_celular(celular):
    # 86 99999-9999
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    # print(resposta)
    return not resposta