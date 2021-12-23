

"""
Curiosidade? Classe dicionário não aceita [ list, set ]
"""

print(conj := {{'nome'}: 'Robson'})  # TypeError: unhashable type: 'set'
print(lista := {[0]: 'desligado'})   # TypeError: unhashable type: 'list'
