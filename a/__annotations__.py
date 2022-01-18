

"""
Objetivo:
    - Criar um dicionário que retorna as classes especificadas nos parâmetros em função
    - Criar um dicionário que retorna as classes especificadas nos atributos de instância em POO
"""


class Person:
    # Métodos de instância com decorador, não aceitam o método
    @property
    def name(self) -> str:
        return self.__name

    @property
    def birthday(self) -> str:
        return self.__birthday

    @name.setter
    def name(self, new_value):
        self.__name = new_value

    @birthday.setter
    def birthday(self, new_value):
        self.__birthday = new_value

    # Atributos de instância aceitam o método quando há tipagem tipagem especificada
    def __init__(self, name: str, birthday: str):
        self.__name = name
        self.__birthday = birthday

    # Métodos de instância sem decorador, aceitam [__annotations__] quando há tipagem especificada
    def name_show(self) -> str:
        return self.__name

    def birthday_show(self) -> str:
        return self.__birthday


if __name__ == '__main__':

    person = Person(name='Lucas', birthday='16/07/1992')
    # Método é aplicável aos métodos: __init__, self sem decorador
    print([1], person.__init__.__annotations__)
    print([2], person.name_show.__annotations__)
    print([3], person.birthday_show.__annotations__)
