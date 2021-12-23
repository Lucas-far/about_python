

"""
Objetivo:
    calcular a média geométrica (não sei exatamente a função disso...)
"""

from statistics import fmean, geometric_mean, mean

v = [1, 2, 3]
v2 = [1.1, 2.2, 3.3]

print([1], geometric_mean(v))
print([1], geometric_mean(v2))

print([2], fmean(v))
print([2], fmean(v2))

print([3], mean(v))
print([3], mean(v2))
