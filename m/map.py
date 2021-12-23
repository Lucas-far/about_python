

"""
Objetivo:
    - função built-in para aplicar uma determinada função em cada item de um objeto iterável
    - pode usar alguns construtores, como: list(), tuple(), set()
    - pode ser substituida pela sintaxe [ filter() ]
"""

if __name__ == '__main__':

    # --------------------------------------- Exemplo com objetos não iteráveis ---------------------------------------
    lst = [1, 2, 3]
    print([1], list(map(lambda x: x + 0.1, lst)))
    print([2], tuple(map(lambda x: x + 0.2, lst)))
    print([3], set(filter(lambda x: f"{x + 0.3:.1f}", lst)))  # forma alternativa para quebrar o padrão

    n_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    n_primos_divididos_2 = tuple(map(lambda x: x / 2, n_primos))
    print(f"[4] Antes: {n_primos}\n[4] Depois: {n_primos_divididos_2}")

    valores_1_20 = [*range(1, 20)]
    print([5], f"Antes: {valores_1_20}")
    print([5], f"Depois: {set(filter(lambda x: not x % 3, valores_1_20))}")

    # ----------------------------------------- Exemplo com objetos iteráveis -----------------------------------------
    linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
    linguagens_cacha_baixa = list(map(lambda x: x.lower(), linguagens))
    print(f"[6] Antes: {linguagens}\n[6] Depois: {linguagens_cacha_baixa}")
