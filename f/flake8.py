

"""
Módulo ### flake8.py

Objetivo:
         analisar se um código/projeto segue as práticas da pep8 do Python

Instalação:
           pip install flake8

Palavra chave: instalar flake8
"""

def python():
    """
    1 - Criar qualquer módulo com algum código para ser analizado
    2 - No terminal: flake8
    """

def django():
    """
    1 - Entre no seu projeto
    2 - Na raiz, criar um módulo: [ .flake8 ]
    3 - Adicionar as seguintes linhas:

        [flake8]
        max-line-length = 120
        exclude=.venv

    4 - No terminal: flake8
    5 - Todos os módulos serão analizados, com exceção das opções salvas no módulo: [ .flake8 ]
    """
