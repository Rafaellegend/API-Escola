def invalid_cpf(cpf):
    return len(cpf) != 11

def invalid_nome(nome):
    return not nome.isalpha()

def invalid_celular(celular):
    return len(celular) != 13