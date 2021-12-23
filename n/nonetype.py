

"""
Objetivo:
     definir uma variável para ter um valor indefinido, para ser modificado futuramente, chamando-a em uma escopo local

Observação:
    1. em Python, uma var não pode ser declarada sem valor, então usa-se a classe do tipo sem tipo (NoneType)
"""

print(nome := None, type(nome))   # Eu quero saber um nome...mas não sei ainda, portanto eu defino o nome como 'nada'

def encapirotar_nome(seu_nome):   # Na função, eu chamo a var do nome, pois é no escopo dela que o nome será definido
    global nome
    nome = seu_nome[::-1]
    return nome

print(encapirotar_nome('Lucas'))  # O nome agora será igual ao argumento da chamada da função
