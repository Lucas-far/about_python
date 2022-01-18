

"""
Objetivo:
    - Converter valor inteiro para sua versão binária

Observação:
    - Os dois primeiros índices do retorno do método, não fazem parte da conversão, então eles são ignorados

Relacionamento:
    @int
"""


def integer_to_binary(value):

    this_message_error = 'Uso somente valores inteiros.'
    try:
        value = bin(value)
        value = str(value)[2:]
        return value
    except ValueError:
        return this_message_error


def integer_to_binary_v2(value):

    this_message_error = 'Uso somente valores inteiros.'
    try:
        value = format(value, 'b')
        return value
    except ValueError:
        return this_message_error


if __name__ == '__main__':
    print([1], integer_to_binary(value=7))
    print([2], integer_to_binary_v2(value=7))
    print([3], integer_to_binary_v2(value=''))
