

"""
Objetivo:
    nesse contexto específico, criar várias chaves com um único valor, através de uma chave = função lambda

Observação:
    1. através da palavra reservada lambda, cria-se um valor padrão para qualquer chave nova criada
    2. chaves são criadas pelos contextos: declaração e print
"""

from collections import defaultdict

print(1, d := defaultdict(lambda: None))
d['a']         # Criação de uma chave sem variável (parece errado, mas funciona)
print(d['b'])  # Criação de uma chave sem variável (dentro do print)
print(2, d)
novo = d['c']  # Criação de uma chave em variável (variável criada e inserida no dicionário)
print(3, d)
