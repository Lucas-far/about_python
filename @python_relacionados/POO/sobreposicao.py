

"""
Objetivo:
    Criar uma segunda classe (filho), que herda de uma primeira (pai), atributos de instância, classe, métodos
"""

class Pai:
    bicicleta = 'MTB Specialized Rockhopper'

    def __init__(self, nome, sobrenome):
        self.__nome = nome
        self.__sobrenome = sobrenome

    def cumprimentar(self):
        return f'Prazer, {self.__nome + " " + self.__sobrenome}'

class Filho(Pai):
    bicicleta = 'MTB Specialized'  # sobreposição

    # def __init__(self, nome, sobrenome):
    #     super().__init__(nome, sobrenome)

    def cumprimentar(self):
        this_method_father = super().cumprimentar()     # herda o método da classe pai
        return f'{this_method_father}. Aperto de mão!'  # sobreposição, concatena-se o método pai ao método filho

if __name__ == '__main__':
    obj_pai = Pai('João', 'Freitas')
    print([1], obj_pai.bicicleta)
    print([2], obj_pai.cumprimentar())
    obj_filho = Filho('Marcelo', 'Freitas')
    print([1], obj_filho.bicicleta)
    print([2], obj_filho.cumprimentar())
