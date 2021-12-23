

"""
Objetivo
     retornar um dicionário da variável de um objeto instanciado
"""

class Bandeira:
    def __init__(self, cores, altura_largura):
        self.cores = cores
        self.altura_largura = altura_largura

# Declaração
exemplo = Bandeira(['verde', 'amarelo', 'azul', 'branco'], (12, 24)).__dict__
print(1, exemplo)

# Print
exemplo2 = Bandeira(['branco', 'rosa', 'amarelo'], (12, 24))
print(2, exemplo2.__dict__)
