

"""
Objetivo:
    retornar a raiz quadrada de um valor inteiro

Objetivo 2:
    retornar a parcela inteira de um valor inteiro que não possui raiz exata,

Observação:
    1. tanto para o objetivo 1 e 2, os valores podem estar sozinhos ou em um iterável que contenha somente inteiros
    1. exemplificando o objetivo 2
       EXEMPLO:
           10 não têm uma raiz exata
           o método isqrt() faz cálculos até chegar ao inteiro, cuja multiplicação é a mais próxima de 10...
           o mais próximo é [ 3 x 3 = 9 ], então: isqrt(10) seria 3
"""

from math import isqrt

print([1], isqrt(25))
print([2], v := isqrt(36))
print([3], [isqrt(each_number) for each_number in [9, 169, 64, 100, 144]])  # método em comprehension lista
print([4], tuple((isqrt(each_number) for each_number in (225, 484, 729))))  # método em comprehension gerador

# exemplo de comportamento do método com dados que não possuem raiz exata
print([5], {isqrt(each_number) for each_number in [10, 20, 30, 40, 50]})
