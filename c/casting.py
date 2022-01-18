

"""
Objetivo:
    - Converter uma classe para outra
"""


tupla = ()
print([1], tupla)
tupla = set(tupla)
print([2], tupla)
tupla = list(tupla)
print([3], tupla)
tupla = dict(chave=tupla)
print([4], tupla)
tupla = tuple(tupla.items())
print([5], tupla)
tupla = str(tupla)
print([6], tupla)
tupla = bool(tupla)
print([7], tupla)
tupla = int(tupla)
print([8], tupla)
tupla = float(tupla)
print([9], tupla)
tupla = complex(tupla)
print([10], tupla)
