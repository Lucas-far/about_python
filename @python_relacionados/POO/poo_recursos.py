

class Cachorro:  # criação da classe
    # atributos de classe
    # frases = [
    #     'Eu não sou seu amigo, kkk',
    #     'Eu estou cansado, vou dormir :)!',
    #     'Onde está o meu lanche? U.U',
    #     'Eu acho que vou banhar, não quero T-T'
    # ]

    frases = {
        'frase1': 'Eu não sou seu amigo, kkk',
        'frase2': 'Eu estou cansado, vou dormir :)!',
        'frase3': 'Onde está o meu lanche? U.U',
        'frase4': 'Eu acho que vou banhar, não quero T-T'
    }

    @classmethod
    def dizer_frase(cls, index):  # atributo de classe / imprimir
        return cls.frases[index]

    @classmethod
    def mudar_frase(cls, index, nova_frase):  # atributo de classe / alterar
        cls.frases[index] = nova_frase

    @staticmethod
    def mensagem():  # método estático (não está ligado aos atributos de classe ou instância)
        return f'BEM-VINDO \ ^^ /'

    @property
    def nome(self):  # atributo de instância / retornar / antes de __init__ / mandatorio: return e .__
        return self.__nome

    @nome.setter
    def nome(self, novo_valor):  # atributo de instância / alterar / anterior / mandatorio: .__
        self.__nome = novo_valor

    def __init__(self, nome: str = 'vazio', *cores):  # método inicializador / atributos de instância
        self.__nome = nome                            # declaração dos atributos (instância e classe)
        self.__cores = list(cores)
        Cachorro.altura = 'atributo de classe'        # definindo um atrib. classe (não recomendado fazer aqui)
        print([1], self._exibir_cores())              # método privado / chamada

    def _exibir_cores(self):  # método privado
        return self.__cores

if __name__ == '__main__':
    rufus = Cachorro('Rufus', 'preto', 'branco')
    lufus = Cachorro('Lufus', rufus._Cachorro__cores)       # obj2 recebendo obj1 como um dos parâmetros
    print([2], rufus.__dict__)
    # print([3], rufus.dizer_frase(0))                      # atributo de classe (chamada)
    print([3], rufus.dizer_frase('frase4'))
    # rufus.mudar_frase(0, 'Eu quero brincar, humano! :P')  # atributo de classe (alteração)
    rufus.mudar_frase('frase4', 'Eu quero brincar, humano! :P')
    # print([4], rufus.dizer_frase(0))
    print([4], rufus.dizer_frase('frase4'))
    rufus.idade = 10                                      # criação de atributo dinâmico
    print([5], rufus.idade)
    print([6], rufus.mensagem())                                      # def mensagem (uso)
    print([7], rufus.nome)                                # def nome (uso) (@property)
    rufus.nome = 'Leonidas'                               # def nome (uso) (@nome.setter)
    print([8], rufus.nome)
    print([9], rufus.__init__.__annotations__)            # mostrar tipos em def __init__
    print([10], rufus.__dict__)
    del rufus.idade                                       # deletar atributo dinâmico, ou classe, ou de instância)
    print([11], rufus.__dict__)
    print([12], lufus.__dict__)
