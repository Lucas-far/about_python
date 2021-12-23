

def obs():
    """ O unittest já vêm configurado com o Python, portanto o requisito é a configuração """


def configuracao():
    """
    - Criar um [ pacote python ] na raiz do repositório local, com o nome [ tests ] (nome é opcional)
    - Criar um módulo python [ tests ] ou o nome que desejar
    - Importar a ferramenta: from unittest import TestCase
    - Importar os métodos a serem testados
    """


def configuracao_esqueleto():
    """
    - Criar uma classe com a sintaxe [ camel case ] e de nome similar ao método [ def falar ] [ class TestFalar ]
    - Há dois métodos, um para criar um objeto para testes e o outro para criar um objeto normal, e compará-los
    - Há variadas formas de comparar, mas as que eu acho melhor são [ self.assertEqual() ] [ self.assertNotEqual() ]

    EXEMPLO

    class TestMtdDaySuffixManager(TestCase):

    def setUp(self):
        self.object_for_test = mtd_day_suffix_manager(day='1')

    def test_mtd_day_suffix_manager(self):
        self.object = mtd_day_suffix_manager(day='1')
        self.object2 = mtd_day_suffix_manager(day='2')
        self.assertEqual(self.object_for_test, self.object)
        self.assertNotEqual(self.object_for_test, self.object2)
    """


def execucao_do_test():
    """
    - (Opção 1) Podem ser no próprio módulo onde há os testes (só pode ser testado um por vez)
    - (Opção 2) Via terminal, pela sintaxe [ python -m unittest discover nome da pasta ]
    """
