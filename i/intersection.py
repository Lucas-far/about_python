

"""
Objetivo:
    comparar e retornar dados idênticos de uma var conjunto alvo em relação a outra(s) passadas como parâmetro
"""

# @set

print([1], {False, None, True}.intersection({8, 9, 10}))           # retorno quando não há qualquer similaridade
print([2], {False, None, True}.intersection({('t',), 's', None}))  # retorno quando há qualquer similaridade

# Em caso de + de 1 parâmetro, só há retorno se: algum dado em {a} exister em {b} e em {c} simultaneamente
print([3], {'a', 'b', 'c', 'd'}.intersection({'a', 'f'}, {'a', 'h'}))  # retorno quando há qualquer similaridade
