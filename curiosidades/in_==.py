

"""
Curiosidade? Mostrar a diferença de funcionamento dos operadores [ in ] e [ == ] em classes iteráveis e não
"""

dado_string, dado_inteiro = '7', 7
lista, lista2 = ['7'], [7]


print([1], dado_string in lista)     # '7' in ['7']
print([2], dado_string == lista[0])  # '7' == '7'


print([3], dado_inteiro == lista2[0])  # 7 == 7
print([4], dado_inteiro in lista2)     # 7 in [7]

# CONCLUSÃO: Se for usar [ in ] a procura é geral, e [ == ] é procura específica
