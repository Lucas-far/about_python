

"""
Curiosidade? substituir valores de lista por outros dentro dela
"""

lista = [False, None, True]

print([1], lista)
lista[0], lista[2] = lista[1], lista[1]
print([2], lista)
