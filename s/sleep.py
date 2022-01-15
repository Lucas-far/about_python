

"""
Objetivo
    Criar pausas no código

Observação:
    O método pode ser usado antes do [ print() ]
"""

from time import sleep


def show_with_interval(*args, delay):
    for data in args:
        print(data, end=' ')
        sleep(delay)  # Uso aqui


if __name__ == '__main__':
    show_with_interval('Python', 'é', 'uma', 'linguagem', 'de', 'programação', delay=1)
