

# ------------------------------------------------------ Aula 98 ------------------------------------------------------
class Pessoa:

    # Na ausência de um parâmetro [self], o método é entendido como estático, por isso [staticmethod]
    @staticmethod
    def falar_v2(sentence):
        return sentence

    # Permite um atributo específico poder ser chamado pelo seu objeto
    @property
    def nome(self):
        return self.__nome

    # Permite um atributo específico pode ser alterado por reatribuição (nome do atributo.setter)
    @nome.setter
    def nome(self, new_value):
        self.__nome = new_value

    @property
    def nacionalidade(self):
        return self.__nacionalidade

    # O [self] é um indicador de que algum atributo de instância será chamado
    def falar(self, sentence):
        return f'{self.__nome} disse: {sentence}'

    # O atributo [nacionalidade], por ter um valor pré-definido, não é obrigado a ser chamado no objeto
    def __init__(self, nome, nacionalidade='Brasileiro', comendo=False, falando=False):
        self.__nome = nome
        self.__nacionalidade = nacionalidade
        self.__comendo = comendo
        self.__falando = falando

    def comer(self, alimento):
        if not self.__comendo:
            self.__comendo = True
            print(f'{self.__nome} está comendo um(a) {alimento}')

    def parar_comer(self):
        if self.__comendo:
            self.__comendo = False
            print(f'{self.__nome} parou de comer')


if __name__ == '__main__':
    pessoa_1 = Pessoa(nome='Fabrício')
    print(pessoa_1.falar(sentence='Eu gosto de Python'))
    print(pessoa_1.nome)
    print(pessoa_1.nacionalidade)
    pessoa_1.nome = 'Lucas'
    print(pessoa_1.nome)
    pessoa_1.comer(alimento='biscoito')
