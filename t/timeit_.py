

"""
Objetivo:
    testar o tempo de execução de códigos: em string, literal, variável, em função

Documentação:
    - https://docs.python.org/3/library/timeit.html#examples
"""


def count_from(this_point, to_this):

    while this_point < to_this:
        print(this_point)
        this_point += 1


if __name__ == '__main__':
    from timeit import timeit, repeat
    # Referenciado
    print([1], timeit(stmt="count_from(1, 1001)", setup="from __main__ import count_from", number=1))

    # Literal
    print([2], timeit(stmt="[data for data in tuple(range(1, 10001))]", number=1))

    # Em variável
    var = "[data for data in tuple(range(1, 10001))]"
    print([3], timeit(stmt=var, number=1))

    # Último parâmetro chamado, para evitar importações
    print([4], timeit(stmt="[data for data in tuple(range(1, 10001))]", number=1, globals=globals()))

    # Armazenar numa lista quantas vezes cada execução aconteceu
    print([5], repeat(stmt="[data for data in tuple(range(1, 10001))]", number=1, repeat=100))
