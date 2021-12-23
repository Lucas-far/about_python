

"""
Objetivo:
    decorador indicador de que uma classe não pode ter a si, ou seus métodos, herdados, porém não bloqueia a ação

Observação:
    1. no mypy, esse erro é acusado, mas não é impedido
"""

from typing import final

def fonte():
    """
    Curso  # Programação em Python do básico ao avançado
    Seção  # Seção 24:Novidades do Python 3.8
    Aula   # 169. Tipos de dados mais precisos
    Tempo  # 20:50
    """

@final
class Professor:  # Essa classe não deveria ser herdada
    def __init__(self, nome):
        self.nome = nome

    @final
    def apresentar(self):  # Esse método não deveria ser sobescrito
        print(f'Eu sou {self.nome}, o seu professor de Álgebra')

class Aluno(Professor):    # classe [ Aluno ] não deve herdar de [ Professor ]
    def apresentar(self):  # Esse método não deve ser sobescrito
        print(f'Eu sou {self.nome}, um aluno de Álgebra')

aluno = Aluno('Alfredo')
aluno.apresentar()

def mypy() -> None:
    """
    final.py:30: error: Cannot inherit from final class "Professor"
    Found 1 error in 1 file (checked 1 source file)
    """
print(mypy.__doc__)
