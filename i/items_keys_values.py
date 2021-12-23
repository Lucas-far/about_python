

"""
Objetivo
    mostrar formas diferentes de iterar sob um dicionário, usando métodos diferentes
"""

d = {'nome': 'Alfredo Costa', 'idade': 43, 'calvice': False, 'atleta': True}

# Forma normal (apenas a chave é exibida)
for x in d:
    print('sem método ||', x)

# Forma .items() (chave e valor são exibidos, mas em forma de tupla)
for x in d.items():
    print('.items() ||', x)

# Forma .keys() (igual a forma normal)
for x in d.keys():
    print('.keys() ||', x)

# Forma .values() (apenas o valor é exibido)
for x in d.values():
    print('.values() ||', x)
