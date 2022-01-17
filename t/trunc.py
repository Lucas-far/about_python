

"""
Objetivo:
    - Retornar a parte inteira de um valor flutuantes
"""


def return_integer_piece(value):

    from math import trunc

    this_msg_error = 'O dado fornecido é incompatível com este método'

    try:
        piece = trunc(value)  # Uso aqui
        return piece
    except TypeError:
        return this_msg_error


if __name__ == '__main__':
    print(return_integer_piece(value=7.7))
    print(return_integer_piece(value='7.7'))
    print(return_integer_piece(value=['7.7']))
