

"""
Objetivo:
    não sei...
"""

from collections import OrderedDict

# Dicionários ordenados comparados, com dados iguais, mas ordens diferentes, não são considerados a mesma coisa
d = OrderedDict({'a': 'b', 'c': 'd', 'e': 'f'})
d2 = OrderedDict({'e': 'f', 'a': 'b', 'c': 'd'})
print([1], f'{d == d2 = }')

# Dicionários comuns comparados, com dados iguais, mas ordens diferentes, são considerados a mesma coisa
d3 = {'1': 1, '2': 2, '3': 3}
d4 = {'3': 3, '1': 1, '2': 2}
print([2], f'{d3 == d4 = }')
