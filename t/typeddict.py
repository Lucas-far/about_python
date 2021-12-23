

"""
Objetivo:
    tornar uma classe em POO, passível de instanciar objetos em forma de dicionário

Observação:
    1. nos valores, são passados somente os tipos
    2. na instanciação do objeto, é mandatório argumentos nomeados (keyword arguments)
    3. podem-se intanciar um objeto de uma classe existente com parâmetros inexistentes, mas isso é um erro
"""

from typing import TypedDict

def fonte():
    """
    Curso  # Programação em Python do básico ao avançado
    Seção  # Seção 24:Novidades do Python 3.8
    Aula   # 169. Tipos de dados mais precisos
    Tempo  # 26:20
    """

# Forma normal
class Dados2:
    def __init__(self, nome: str, idade: int, esportes: tuple):
        self.nome = nome
        self.idade = idade
        self.esportes = esportes
print([1], objeto3 := Dados2('Lucas', 28, ('tênis', 'tênis de mesa', 'badmintom', 'ciclismo')).__dict__)

# Forma TypedDict
class Dados(TypedDict):
    nome: str
    idade: int
    esportes: tuple

print([2], objeto := Dados(nome='Lucas', idade=28, esportes=('tênis', 'tênis de mesa', 'badmintom', 'ciclismo')))

# Se atributos inexistentes forem chamados, a IDE não retorna erro, mas 'mypy' retorna um erro
print([3], objeto2 := Dados(genero='Masculino', cor='pardo'))

# Retorno mypy
"typeddict.py:36: error: Extra keys ('genero', 'cor') for TypedDict 'Dados'"
"Found 1 error in 1 file (checked 1 source file)"
