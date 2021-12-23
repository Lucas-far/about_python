

"""
Objetivo:
    retornar docstring matriz de um módulo alvo ou de uma função dentro do módulo alvo

Observação:
    1. método não precisa de print
    2. para ser usado para ver a docstring matriz de um módulo, é preciso usar o console python

       SINTAXE:
           terminal / python / import módulo / help(módulo)

       SINTAXE CONTEXTUAL NESSE MÓDULO:
           terminal / python / from PYTHON.h import help_ / help(help_)
"""

def criar_dicio(chave, valor):
    """ Criar um dicionário """
    return {chave: valor}

help(criar_dicio)           # retornando docstring de um função dentro de um módulo alvo
print(criar_dicio.__doc__)  # outra forma
