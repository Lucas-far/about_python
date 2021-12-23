

"""
Objetivo:
    retornar a valor flutuante mais aproximado possível de um valor inteiro que não possui raiz exata

Objetivo 2:
    retornar o valor flutuante de um valor inteiro que possui raiz exata

Observação:
    1. o método srqt() parece-se com o método isqrt() quando o caso é raiz inexata, mas não é a mesma coisa
"""

from math import sqrt

print([1], sqrt(25))       # quando o valor possui raiz exata, retorn-se a forma flutuante
print([2], v := sqrt(10))  # quando o valor não possui raiz exata, retorna-se a forma flutuante mais próxima

# Exemplos em comprehension com valores de raiz exata
print([3], [sqrt(each_number) for each_number in [9, 169, 64, 100, 144]])
print([4], tuple((sqrt(each_number) for each_number in (225, 484, 729))))

# Exemplo em comprehension com valores de raiz não exata
print([5], {sqrt(each_number) for each_number in [10, 20, 30, 40, 50]})
