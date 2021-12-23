

"""
Objetivo:
    remover de uma classe lista, o último índice ou um índice específico

Objetivo 2:
    remover de uma classe dicionário, uma chave específica

Objetivo 3:
    remover de uma classe conjunto, um dado aleatório

Observação:
    1. esse método pode ser combinado ao método .index() para pegar índices específicos de uma lista
    2. esse método possui um primo: .popitem()
    3. método usado em linha, ou com quebras de linha
"""

# @dict @list @set

print([1], d := {'c': 'v', 'c2': 'v2'}), d.pop('c'), print([1], d)  # parâmetro mandatório
print([2], l := ['l', 'i', 's', 't', 'a']), l.pop(), print([2], l)  # parâmetro não mandatório / excluir último índice
print([3], cj := {'s', 'e', 't'}), cj.pop(), print([3], cj)         # parâmetro não mandatório / exclusão aleatória

# Uso mais tradicional
print([4], l2 := [*range(1, 6)])
l2.pop()
print([5], l2)
l2.pop()
print([6], l2)

# Uso em linha
print([7], l3 := ['hahaha', 'kkkkk', 'jajaja', 'blablabla', 'quaquaqua'])
l3.pop(), l3.pop(), l3.pop()
print([8], l3)

# Combinando .pop() + .index() ---> retirar dados especificados
print([9], l4 := ['hahaha', 'kkkkk', 'jajaja', 'blablabla', 'quaquaqua'])
l4.pop(l4.index('hahaha'))
l4.pop(l4.index('quaquaqua'))
print([10], l4)
