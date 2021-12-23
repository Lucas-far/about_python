

"""
Objetivo:
    exibir iteráveis autodestrutivos de exibição única, para ter mais espaço em memória

Observação:
    1. var gerador é, por padrão, uma tupla, que têm seus dados criptografados em um objeto de memória
    2. para descriftografar esses dados, usa-se casting, ou next, na var gerador
    3. uma vez que o objeto é descriptografado, ele só pode ser impresso um vez, pois os dados são destruidos
    4. para rever os dados, a var gerador precisa ser redeclarada
    5. o ciclo é sempre: instanciar, aplicar casting ou next, imprimir, destruir
    6. var gerador é usada por ocupar muito pouco espaço em memória (ver def comparador)
"""

from sys import getsizeof as size

# gerador com casting
semana = (x for x in range(1, 8))  # var gerador criada
print([1], semana)                 # var impressa sem cast, mostra apenas o objeto em memória
print([2], set(semana))            # var impressa com cast, mostra os dados na classe escolhida
print([3], list(semana))           # mas como a exibição é única, a var gerador é zerada
semana = (x for x in range(1, 8))  # a var precisa então ser redeclarada
print([4], list(semana))           # sendo redeclarada, pode ser exibida mais uma vez

# gerador com next
vogais = (x for x in 'aeiou')
print([5], next(vogais))  # usando next, um dado é impresso por vez, isso se next estiver em print
next(vogais)              # o dado seguinte foi chamado, mas não foi exibido, pois não está em print
next(vogais)              # idem
next(vogais)              # idem
print([6], next(vogais))       # estando next no print, o dado atual é exibido

# gerador com if
print([7], g := tuple((x for x in {*range(1, 51)} if not x % 10)))

# gerador com if else
print([8], g2 := tuple(((str(x) + '=' + str(x).replace(str(x), 'sim')) if not x % 7 else 'não' for x in range(17, 27))))

def comparador():
    i = int(input('Insira um número acima de 1 -> '))

    conjunto = {x for x in range(1, i)}
    dicionario = {x: x for x in range(1, i)}
    gerador = (x for x in range(1, i))
    lista = [x for x in range(1, i)]

    print(
        f"""
        Bytes consumidos em conjunto    = [ {size(conjunto)} bytes ]
        Bytes consumidos em dicionário  = [ {size(dicionario)} bytes ]
        Bytes consumidos em lista       = [ {size(lista)} bytes ]
        Bytes consumidos em gerador     = [ {size(gerador)} bytes ]
        """
    )

comparador()
