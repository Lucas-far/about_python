

def objetivo():
    """ Remover um dado específico de uma classe conjunto """


print([1], conj := {0, 'string', None})  # [1] {0, 'string', None}
conj.remove(0)
print([2], conj)                         # [2] {'string', None}

# ------------------------------------------------------ DETALHE ------------------------------------------------------
"O método [ remove ] é similar ao método [ discard ]"
conj.discard('string')
print([3], conj)  # [3] {None}

# ---------------------------------------------------- DETALHE (2) ----------------------------------------------------
conj.remove('strings')  # Se o dado for escrito errado, é gerado [ KeyError ]
