

"""
Objetivo:
    alterar um dado numérico pós-declaração, sem precisar redeclarar uma variável
"""

print([1], soma := 0)
soma += 10  # operador de atribuição '+='
print([1], soma)

print([2], diminuir := 0)
diminuir -= 10  # operador de atribuição '-='
print([2], diminuir)

print([3], multiplicar := 11)
multiplicar *= 2.2  # operador de atribuição '*='
print([3], diminuir)

print([4], dividir := 7)
dividir /= 3  # operador de atribuição '/='
print([4], dividir)

print([5], elevar := 7)
elevar **= 3  # operador de atribuição '**='
print([5], elevar)

print([6], modular := 100)
modular %= 2  # operador de atribuição '%=' (se 0 = número par) (se 1 = número ímpar)
print([6], modular)

print([7], dividir_inteiro := 100)
dividir_inteiro //= 7  # operador de atribuição '//=' (se 0 = número par) (se 1 = número ímpar)
print([7], dividir_inteiro)

# Usando operador de atribuição módular de forma mais abrangente
print([8], [x for x in range(1, 50) if x % 3])      # retirar divisíveis por 3
print([9], [x for x in range(1, 50) if not x % 3])  # filtrar divisíveis por 3
