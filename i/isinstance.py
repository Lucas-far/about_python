

def infos():
    """
    Objetivo
         retornar classe booleana do resultado se um objeto instanciado é herdeiro de uma classe específica

    Observação
        1. esse método retorna True quando há herança entre classes, e retorna False quando não há
    """

class Nome:
    def __init__(self, nome):
        self.__nome = nome

# Herança de primeiro grau
class Sobrenome(Nome):                    # herda da classe [ Nome ]
    def __init__(self, nome, sobrenome):  # atributos locais e herdados devem ser inseridos
        super().__init__(nome)            # sintaxe obrigatória para a classe herdeira, com os atr. herdados
        self.__sobrenome = sobrenome      # declaração do atributo de instância local

# Herança de segundo grau
class Email(Sobrenome):                          # herda da classe [ Sobrenome ]
    def __init__(self, email, nome, sobrenome):  # atributos locais e herdados devem ser inseridos
        super().__init__(nome, sobrenome)        # sintaxe obrigatória para a classe herdeira, com os atr. herdados
        self.__email = email                     # declaração do atributo de instância local

class Mensagem:
    def __init__(self, mensagem):
        self.__mensagem = mensagem

objeto = Email('Leonardo', 'da Silva', 'leosil@gmail.com')
print([1], isinstance(objeto, Nome))
print([2], isinstance(objeto, Sobrenome))
print([3], isinstance(objeto, Email))
print([4], isinstance(objeto, object))
print([5], isinstance(objeto, Mensagem))  # Quando não há relação de herança
