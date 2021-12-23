

def infos():
    """
    Objetivo
         deletar variáveis, de forma específica (classes iteráveis) ou por inteiro (classes não iteráveis)

    Observações
        1. em caso de classes iteráveis, não funciona com: conjunto, tupla (não possuem indexação)
        2. em caso de classes iteráveis, funciona com: range (caso esteja sob casting)
    """

b, c, d, f, i, l, n, r, cj, s, t = True, 0j, {'c': 'v'}, 0.0, 0, ['list'], None, range(0), {'set'}, 'str', ('tuple',)

print(n)
del n
"print(n)"  # NameError: name 'n' is not defined

print(l)
del l
"print(l)"  # NameError: name 'l' is not defined
