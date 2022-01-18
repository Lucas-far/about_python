

"""
Objetivo:
    - Executar subtração ou soma entre classes numéricas
"""


class Math:

    @property
    def increase(self):
        return self.__increase

    @increase.setter
    def increase(self, new):
        self.__increase = new

    @property
    def decrease(self):
        return self.__decrease

    @decrease.setter
    def decrease(self, new):
        self.__decrease = new

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new):
        self.__value = new

    def __init__(self, increase, decrease, value):
        self.__increase = increase
        self.__decrease = decrease
        self.__value = value

    def __add__(self, other_value):
        if self.__increase:
            self.__value = self.__value + other_value
        if self.__decrease:
            self.__value = self.__value - other_value


if __name__ == '__main__':
    this_object = Math(increase=True, decrease=False, value=7)
    print(this_object.value)
    this_object.__add__(3)
    print(this_object.value)
    this_object.increase = False
    this_object.decrease = True
    this_object.__add__(8)
    print(this_object.value)
