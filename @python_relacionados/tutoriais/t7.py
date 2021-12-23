

"""
Objetivo:
    mostrar a diferença de comportamento entre os métodos: fmean() & mean()

Observação:
    1. como cálculo de média necessita mais de um valor, então o método só funciona com dados dentro de iteráveis
    2. com fmean(), o retorno sempre será flutuante, independente de ser real ou não
    3. com mean(), o retorno sempre será inteiro, independnente de ser real ou não
"""
# todo Tutorial 7

from statistics import fmean, mean

# Diferença de comportamento dos métodos em relação à presença de valores não reais
print([1], 'fmean ||', fmean([1, 2, 3]))
print([2], 'mean  ||', mean([1, 2, 3]))
print([3], 'fmean ||', fmean([1.1, 2.2, 3.3]))
print([4], 'mean  ||', mean([1.1, 2.2, 3.3]))
