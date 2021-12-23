

"""
Objetivo:
    verificar se um número é par ou ímpar

Objetivo 2:
    analizar iteráveis para filtrar dados
"""

# Verificando por ou ímpar
v = 0
if v % 2 == 0:
    print(f'O número {v} é par')
else:
    print(f'O número {v} é ímpar')

# Exemplos de operações modular
print([1], [x for x in [*range(1, 28)] if x % 7 == 0])  # divisíveis por 7
print([2], [x for x in [*range(1, 28)] if not x % 7])   # divisíveis por 7

print([3], [x for x in [*range(1, 28)] if x % 2])       # filtragem de ímpares
print([5], [x for x in [*range(1, 28)] if x % 2 == 1])  # filtragem de ímpares

print([4], [x for x in [*range(1, 28)] if not x % 2])   # filtragem de pares
print([6], [x for x in [*range(1, 28)] if x % 2 == 0])  # filtragem de pares

# Outros exemplos
numero = 2_892_458
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
dezena_milhar = numero // 10_000 % 10
centena_milhar = numero // 100_000 % 10
milhao = numero // 1_000_000 % 10

relatorio = f"""
    Unidade: [ {unidade} ]    Dezena: [ {dezena} ]    Centena: [ {centena} ]    Milhar: [ {milhar} ]
    Dezena de milhar: [ {dezena_milhar} ]    Centena de milhar: [ {centena_milhar} ]    Milhão: [ {milhao} ]
    """

print(relatorio)
