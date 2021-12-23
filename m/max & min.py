

"""
Objetivo:
    retornar o dado mínimo em uma classe iterável, especificando início ou início e fim

Objetivo 2:
    retornar o dado máximo em uma classe iterável, especificando início ou início e fim

Observação:
    1. o método, por padrão, age procurando o menor ou maior dado dentro de um iterável
    2. o método, pode fazer uma varredura mais específica, se um slice for especificado
    3. uso em strings, min() filtra o menor dado alfabético, e max() filtra o maior
"""

t = ('not False', 'False', 'True', 'not True')
l = ['f', 'x', 'l', 'b', 'd', 's', 't', 'y']

print([1], max([*range(1, 11)]))  # uso normal, sem espeficar slice
print([2], min(t[1:]))            # procurar menor dado a partir do índice 4
print([3], max(l[1:4]))           # procurar maior dado do índice 1 ao 3

# Slices mais complexos
print([4], l[0:7:2])              # a partir do 0, até 6, saltos de 2
print([5], min(l[0:7:2]))         # ver [4], para melhor entendimento
print([6], l[0::3])               # a partir do 0, até fim, saltos de 3
print([7], max(l[0::3]))          # ver [6], para melhor entendimento
print([8], l[:6:1])               # a partir do 0, até 5, saltos de 1
print([9], min(l[:5:1]))          # ver [8], para melhor entendimento
