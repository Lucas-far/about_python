

"""
Objetivo
    enumerar cada dado de um iterável, dentro ou fora de um loop for

Observações
    1. para funcionar em um loop for, é preciso criar uma var interna para o método (primeira var)
"""

# Uso normal
print(1, d := dict(enumerate('Cleber')))
print(2, l := list(enumerate('Diego')))
print(3, t := tuple(enumerate('Helena')))
print(4, cj := set(enumerate('Pedrita')))

print('========== BLOCO DE DIVISÃO ==========')

# Uso em loop for com uma var no loop
for x in enumerate(cj):
    print(x)

print('========== BLOCO DE DIVISÃO 2 ==========')

# Uso em loop for com duas vars no loop
for y, x in enumerate(cj):
    print(y, x)

print('========== BLOCO DE DIVISÃO 3 ==========')

# Uso em loop for com duas vars no loop (usando end="")
for y, x in enumerate(cj):
    print(y, x, end=' ')
