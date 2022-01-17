

"""
Objetivo:
    - Gerar números flutuantes específicos, usando parâmetros inteiros, + ou -

Observação:
    - Por gerar valores flutuantes extensos, o método [round] pode ser aplicado para diminuir o número de casas
"""


def generate_float(from_this_point, to_this_point, decimal_places):
    from random import uniform

    this_msg_error = 'O tipo de dado informado é incompatível com este método. Use valores inteiros ou flutuantes.'

    try:
        value = round(uniform(from_this_point, to_this_point), decimal_places)
        return value
    except TypeError:
        return this_msg_error


if __name__ == '__main__':
    print(generate_float(from_this_point=0, to_this_point=1, decimal_places=2))
