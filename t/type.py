

"""
Objetivo:
    - Informar o tipo de um dado em Python
"""


def tell_the_data_type(data_):

    return type(data_)


if __name__ == '__main__':

    from collections import deque, Counter

    class Modelo:
        def __init__(self, nome):
            self.__nome = nome

    object_ = Modelo(nome='Python')

    print(tell_the_data_type(data_=True))
    print(tell_the_data_type(data_=None))
    print(tell_the_data_type(data_=1j))  
    print(tell_the_data_type(data_=1))
    print(tell_the_data_type(data_=1.0))
    print(tell_the_data_type(data_={'conjunto'}))
    print(tell_the_data_type(data_=Counter('iterável')))
    print(tell_the_data_type(data_=deque(['deque'])))
    print(tell_the_data_type(data_={'dicionário': None}))
    print(tell_the_data_type(data_={'dicionário': None}.items()))
    print(tell_the_data_type(data_={'dicionário': None}.keys()))
    print(tell_the_data_type(data_={'dicionário': None}.values()))
    print(tell_the_data_type(data_=['lista']))
    print(tell_the_data_type(data_='string'))
    print(tell_the_data_type(data_=('tupla',)))
    print(tell_the_data_type(data_=range(1, 2021)))
    print(tell_the_data_type(data_=object_))