

"""
Curiosidade? Conjunto aceita [ str, tuple, range ] e rejeita [ set, dict, list ]
"""


# ------------------------------------------------------ Aceitos ------------------------------------------------------
print(string := {'string'})
print(tupla := {('tupla',), ('tupla2',)})
print(range_ := {*range(1, 6)})

# ------------------------------------------------------ Negados ------------------------------------------------------
# print(conjunto := {{'conjunto'}})  # TypeError: unhashable type: 'set'
# print(dicio := {{'dicio': None}})  # TypeError: unhashable type: 'dict'
# print(lista := {['lista']})        # TypeError: unhashable type: 'list'
