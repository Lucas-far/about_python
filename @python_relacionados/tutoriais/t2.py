

"""
Objetivo
    declarar muitas variáveis ou literais em linha, para economizar espaço em linha
"""
# todo Tutorial 2

complexo, conjunto, dicio, lista, nenhum, range_, string, tupla = \
    7j, {1, 4, 2020}, {'ano': 2020}, [1, 4, 2020], None, tuple(range(1, 11)), ('1', '4', '2020'), '01/04/2020',
print(
    f"""
    Complexo: {complexo}
    Conjunto: {conjunto}
    Dicionário: {dicio}
    Lista: {lista}
    Dado sem tipo: {nenhum}
    Range: {range_}
    String: {string}
    Tupla: {tupla}
    """
    )
