

"""
>>> motor = Motor()
>>> motor.calcular_velocidade()
0

>>> motor.acelerar()
>>> motor.calcular_velocidade()
1

>>> motor.acelerar()
>>> motor.calcular_velocidade()
2

>>> motor.frear()
>>> motor.calcular_velocidade()
0





>>> sentido = Sentido()
>>> sentido.mostrar_coordenada()
'Norte'

>>> sentido.ir_direita()
>>> sentido.mostrar_coordenada()
'Leste'

>>> sentido.ir_direita()
>>> sentido.mostrar_coordenada()
'Sul'

>>> sentido.ir_direita()
>>> sentido.mostrar_coordenada()
'Oeste'

>>> sentido.ir_direita()
>>> sentido.mostrar_coordenada()
'Norte'


>>> sentido.ir_esquerda()
>>> sentido.mostrar_coordenada()
'Oeste'

>>> sentido.ir_esquerda()
>>> sentido.mostrar_coordenada()
'Sul'

>>> sentido.ir_esquerda()
>>> sentido.mostrar_coordenada()
'Leste'

>>> sentido.ir_esquerda()
>>> sentido.mostrar_coordenada()
'Norte'





>>> carro = Carro(sentido, motor)
>>> carro.calcular_velocidade()
0

>>> carro.acelerar()
>>> carro.calcular_velocidade()
1

>>> carro.acelerar()
>>> carro.calcular_velocidade()
2

>>> carro.frear()
>>> carro.calcular_velocidade()
0

>>> carro.calcular_sentido()
'Norte'

>>> carro.ir_direita()
>>> carro.calcular_sentido()
'Leste'

>>> carro.ir_esquerda()
>>> carro.calcular_sentido()
'Norte'

>>> carro.ir_esquerda()
>>> carro.calcular_sentido()
'Oeste'
"""

# todo Dados complementares para esse módulo:
#     home/lucas/PycharmProjects/recursos/PYTHON/POO/doctest_infos.py

class Carro:

    def __init__(self, sentido, motor):
        self.__motor = motor
        self.__sentido = sentido

    def acelerar(self):
        self.__motor.acelerar()

    def frear(self):
        self.__motor.frear()

    def calcular_velocidade(self):
        return self.__motor.calcular_velocidade()

    def calcular_sentido(self):
        return self.__sentido.mostrar_coordenada()

    def ir_direita(self):
        self.__sentido.ir_direita()

    def ir_esquerda(self):
        self.__sentido.ir_esquerda()

NORTE = 'Norte'
LESTE = 'Leste'
SUL = 'Sul'
OESTE = 'Oeste'

class Sentido:

    ir_direita_logica = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    ir_esquerda_logica = {NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE}

    def __init__(self):
        self.__coordenada = NORTE  # atributo de instância não obrigatório (objeto pode ser passado vazio)

    def mostrar_coordenada(self):
        return self.__coordenada

    def ir_direita(self):
        self.__coordenada = self.ir_direita_logica[self.__coordenada]
        # if self.__sentido == 'Norte':
        #     self.__sentido = 'Leste'
        # elif self.__sentido == 'Leste':
        #     self.__sentido = 'Sul'
        # elif self.__sentido == 'Sul':
        #     self.__sentido = 'Oeste'
        # else:
        #     self.__sentido = 'Norte'

    def ir_esquerda(self):
        self.__coordenada = self.ir_esquerda_logica[self.__coordenada]
        # if self.__sentido == 'Norte':
        #     self.__sentido = 'Oeste'
        # elif self.__sentido == 'Oeste':
        #     self.__sentido = 'Sul'
        # elif self.__sentido == 'Sul':
        #     self.__sentido = 'Leste'
        # else:
        #     self.__sentido = 'Norte'

class Motor:

    def __init__(self):
        self.__velocidade = 0  # atributo de instância não obrigatório (objeto pode ser passado vazio)

    def acelerar(self):
        self.__velocidade += 1

    def frear(self):
        self.__velocidade -= 2
        self.__velocidade = max(0, self.__velocidade)
        # if self.__velocidade < 0:
        #     self.__velocidade = 0

    def calcular_velocidade(self):
        return self.__velocidade

if __name__ == '__main__':
    pass

def tutorial_classe_motor():
    """
    --------------------------------------------------------------------------------------------------------------------
    CLASSE: MOTOR
    --------------------------------------------------------------------------------------------------------------------
    1. Uma classe [ Motor ] é criada
    2. Nota-se que nao há atribs. inst. dentro do método __init__
    3. Porém, se no escopo de declaração há [ self.var ], esta será interpretada como atrib. inst. (não obrigatória)
    4. Os três métodos nela existentes, serão herdados futuramente ()
    """

def tutorial_classe_sentido():
    """
    --------------------------------------------------------------------------------------------------------------------
    CLASSE: SENTIDO
    --------------------------------------------------------------------------------------------------------------------
    1. Uma classe [ Sentido ] é criada
    2. Nota-se que nao há atribs. inst. dentro do método __init__
    3. Porém, se no escopo de declaração há [ self.var ], esta será interpretada como atrib. inst. (não obrigatória)
    4. Acima da chamada da classe, há vars constantes que são chamadas em seu escopo

    5. Há dois atribs. classe, que são vars dicionário, e elas são influenciadas pelas vars contantes
       Uma das vars constantes é passada como valor do atrib. inst. [ coordenada ]
       Quando o método [ ir_direita() / ir_esquerda() ] for usado, o dicionário troca para a nova coordenada
           Por exemplo:
                       obj = Sentido('Sul')
                       print(obj.coordenada)  # 'Sul'
                       print(obj.ir_esquerda())
                       self.coordenada = 'Leste'
    """

def tutorial_classe_carro():
    """
    --------------------------------------------------------------------------------------------------------------------
    CLASSE: CARRO
    --------------------------------------------------------------------------------------------------------------------
    1. Essa classe é quem executa o conceito de COMPOSIÇÃO

    2. E como acontece essa composição?

       pelos 2 objetos [ motor & sentido ] que foram criados anteriormente, das classes [ Motor & Sentido ]
       esses 2 objetos são passados como atribs. inst., dentro da classe [ Carro ]
       isso significa que, através do objeto, podemos chamar: [ atribs. inst. / atribs. classe / métodos ]

       .................................................................................................................
       EXEMPLO:
               def calcular_velocidade(self):
                   return self.__motor.calcular_velocidade()

       Através do objeto [ motor ] eu chamo um método que chama o atrib. inst. [ velocidade ], da classe [ Motor ]

       EXEMPLO 2:
                 def ir_direita(self):
                     self.__sentido.ir_direita()

       Através do objeto [ sentido ] eu chamo um método que altera o atrib. inst. [ coordenada ], da classe [ Sentido ]

       EXEMPLO 3:
                 def frear(self):
                     self.__motor.frear()

       Através do objeto [ motor ] eu chamo um método que altera o atrib. inst. [ velocidade ], da classe [ Motor ]
       .................................................................................................................

    3. Os métodos dessa classe são todos herdados, através dos objetos [ motor & sentido ], passados como atribs. inst.
    """
