

"""
Objetivo:
    - Converter classes numéricas de valor negativo para sua versão positiva

Relacionamento:
    @int @float @complex
"""


def turn_value_into_positive(value):

    this_msg_error = 'O tipo de dado é incompatível'

    try:
        return value.__abs__()
    except AttributeError:
        return this_msg_error


if __name__ == '__main__':
    print(turn_value_into_positive(value=-1))
    print(turn_value_into_positive(value=-1.1))
    print(turn_value_into_positive(value=-1j))
    print(turn_value_into_positive(value=''))
