

"""
Objetivo:
    retornar o nome da variável de uma classe ou função
"""

def dicio(a, b):
    return {a: b}

print([1], dicio.__name__)

class Dados:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

print([2], Dados.__name__)
