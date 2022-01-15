

"""
Objetivo:
    - Tornar a primeira letra de cada dado string, maiúscula

Observação:
    - Se o dado for iterável, mas não for string, mas ter um dado string, seu índice precisa ser especificado
"""


def capitalize(source_):

    try:
        return source_.title()
    except AttributeError:
        return 'O método não é aplicável a este tipo de dado'


if __name__ == '__main__':
    print(capitalize(source_='python'))
    print(capitalize(source_='...python'))
    print(capitalize(source_=['python']))     # AttributeError
    print(capitalize(source_=1))              # AttributeError
    print(capitalize(source_=['python'][0]))  # Exemplo baseado na observação
