

from unittest import TestCase
# from PYTHON.POO.composicao import Motor, Sentido, Carro
from composicao import Motor, Sentido, Carro


class MotorTestCase(TestCase):
    def test_calcular_velocidade(self):
        motor = Motor()
        self.assertEqual(0, motor.calcular_velocidade())

    def test_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.calcular_velocidade())

    def test_frear(self):
        motor = Motor()
        motor.frear()
        self.assertEqual(0, motor.calcular_velocidade())

class SentidoTestCase(TestCase):
    def test_mostrar_coordenada(self):
        sentido = Sentido()
        self.assertEqual('Norte', sentido.mostrar_coordenada())

    def test_ir_direita(self):
        sentido = Sentido()
        sentido.ir_direita()
        self.assertEqual('Leste', sentido.mostrar_coordenada())

    def test_ir_esquerda(self):
        sentido = Sentido()
        sentido.ir_direita()
        sentido.ir_esquerda()
        self.assertEqual('Norte', sentido.mostrar_coordenada())

class CarroTestCase(TestCase):
    def test_acelerar(self):
        motor = Motor()
        sentido = Sentido()
        carro = Carro(sentido, motor)  # se a ordem for mudada, não funciona
        carro.acelerar()
        self.assertEqual(1, carro.calcular_velocidade())

    def test_frear(self):
        motor = Motor()
        sentido = Sentido()
        carro = Carro(sentido, motor)
        carro.acelerar(), carro.acelerar(), carro.acelerar(), carro.frear()
        self.assertEqual(1, carro.calcular_velocidade())

    def test_calcular_velocidade(self):
        motor = Motor()
        sentido = Sentido()
        carro = Carro(sentido, motor)
        carro.acelerar(), carro.acelerar(), carro.acelerar(), carro.acelerar(),
        self.assertEqual(4, carro.calcular_velocidade())

    def test_calcular_sentido(self):
        motor = Motor()
        sentido = Sentido()
        carro = Carro(sentido, motor)
        carro.ir_esquerda(), carro.ir_esquerda()
        self.assertEqual('Sul', carro.calcular_sentido())

    def test_ir_direita(self):
        motor = Motor()
        sentido = Sentido()
        carro = Carro(sentido, motor)
        carro.ir_esquerda(), carro.ir_esquerda(), carro.ir_direita(),
        self.assertEqual('Oeste', carro.calcular_sentido())

    def test_ir_esquerda(self):
        motor = Motor()
        sentido = Sentido()
        carro = Carro(sentido, motor)
        carro.ir_direita(), carro.ir_direita(), carro.ir_esquerda(),
        self.assertEqual('Leste', carro.calcular_sentido())
