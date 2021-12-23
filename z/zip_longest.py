

"""
Objetivo:
         mesclar em um tupla, dados entre iteráveis, de acordo com seus índices
         porém, se os iteráveis não possuirem mesmo número de índice, o método retorna None junto aos dados restantes

Detalhe(s):
           1 - Não é recomendável usar com classe dict, por não poder repetir chaves
           2 - Não é recomendável usar com classe set, por valores não repetirem-se
"""

from itertools import zip_longest

"Exemplo"  # zip normal com iteráveis de mesma largura
print([1], dict(zip([1, 2, 3], ('a', 'b', 'c'))))

"Exemplo"  # zip normal com iteráveis largura diferente (dados excedentes não são usados)
print([2], dict(zip([1, 2, 3], ('a', 'b', 'c', 'd'))))

"Exemplo"  # zip normal com iteráveis de larguras diferentes (usando zip_longest)
"OBS"      # O iterável menor mostra None, o maior, continua mostrando os dados restantes
print([3], tuple(zip_longest([1, 2, 3], ('a', 'b', 'c', 'd', 'e'))))

"Exemplo"  # zip normal com iteráveis de larguras diferentes (usando zip_longest) + (parâmetro fill_value=)
print([4], tuple(zip_longest([1, 2, 3], ('a', 'b', 'c', 'd', 'e', 'f', 'g'), fillvalue='ausente')))
