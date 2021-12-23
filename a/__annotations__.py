

def infos():
    """
    Uso:
        @poo (programação orientada a objetos)

    Objetivo:
        criar um dicionário que retorna as classes especificadas nos parâmetros em função
        criar um dicionário que retorna as classes especificadas nos atributos de instância em POO
    """


# --------------------------------------- [ __annotations__ ] em um método comum ---------------------------------------
def show_personal_data(name: str, birthday: str):

    return f"""
    ---------------------------------------------------- RELATÓRIO ----------------------------------------------------
    Nome: {name}
    Nascimento: {birthday}"""


# --------------------------------------------- [ __annotations__ ] em POO ---------------------------------------------
class PersonalData:
    # Método de instância com decorador, não aceita o método
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

    # Atributos de instância aceitam o método...se há tipagem tipagem especificada
    def __init__(self, name: str, birthday: str):
        self.__name = name
        self.__birthday = birthday

    # Métodos de instância sem decorador, aceitam o método...se há tipagem especificada
    def name_show(self) -> str:
        return self.__name

    def birthday_show(self) -> str:
        return self.__birthday


if __name__ == '__main__':
    print([1], show_personal_data.__annotations__)     # Não há um objeto, só funciona com a chamada do método literal
    object_ = PersonalData(name='Lucas', birthday='16/07/1992')
    print([2], object_.__init__.__annotations__)       # método built-in [ __init__ ] mandatório
    print([3], object_.name_show.__annotations__)      # método de instância sem decorador consegue chamar
    print([4], object_.birthday_show.__annotations__)  # método de instância sem decorador consegue chamar
    print([5], object_.name)
    object_.name = 'Farias'
    print([6], object_.name)
