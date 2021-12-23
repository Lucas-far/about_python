

"""
Curiosidade? desempacotamento e sintaxe decrescente em classe range
"""

var = range(4)
print([1], var)        # range normal não é exibíbel sem ser desempacotada
print([2], *var)       # range desempacotada
print([3], list(var))  # range desempacotada com construtor

print(tuple(range(5, 0, -1)))   # sintaxe decrescente +
print(tuple(range(7, -8, -1)))  # sintaxe decrescente -
