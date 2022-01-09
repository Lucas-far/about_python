

def fonte():
    """
    https://auth0.com/blog/developing-restful-apis-with-python-and-flask/
    """


# Recomendação de criação de ambiente virtual com: pipenv
def parte_1():
    """
    ------- PROBLEMAS PERCEBIDOS -------
    O tutorial da fonte não parece explicar com clareza todos os passos
    Ao instalar o AV pelo [ pipenv ], o AV é enviado à pasta [ envs ], anteriormente criada para o [ virtualenv ]
    Não faço ideia da razão disso, então foi preciso sair da pasta do projeto, para poder ativar o AV
    Além disso, o nome do AV criado não é controlado por mim: [ flask-CjlE2wDq ]

    ------- INSTALAÇÃO -------
    Pelo Pycharm, já há o [venv] que criar um AV automaticamente nos projetos
    Para logar nele        || [ venv\scripts\activate ]
    Com este logado        || [ pip install pipenv ]
    Sair do venv           || [ deactivate ]
    Entrar no AV do pipenv || [ cd .. ] [ cd .. ] [ cd envs ] [ cd flask-CjlE2wDq ] [ scripts\activate ]
    """


# Configuração confusa
def parte_2():
    """
    Criação de uma pasta na raiz do projeto (mesmo nome da pasta do projeto) (opção minha adicionar: _init)
    Dentro da pasta, criação de um arquivo python [ __init__ ] vazio
    Dentro da pasta, criar arquivo [ index.py ]
    O arquivo [ index.py ] leva o mesmo conteúdo em [ framework_flask/parte_1/def parte_1 ]
    """


# Configuração de um executável
def parte_3():
    """
    1. Na raiz do projeto, criar: [ bootstrap.sh ]
    2. Segundo o tutorial, para torná-lo executável, usar o comando: [ chmod +x bootstrap.sh ]

    ------- PROBLEMA -------
    O comando em (2) não funcionou no Windows

    ------- SOLUÇÃO -------
    https://stackoverflow.com/questions/58941227/does-the-chmod-command-not-work-on-windows-in-gitbash
    Sintaxe que funcionou: [ icacls bootstrap.sh ]
    """


# Configuração do conteúdo do executável
def parte_4():
    """
    ------- PROBLEMA -------
    A sintaxe parece ser Linux e houve problemas com o AV pipenv

    ------- SINTAXE ORIGINAL DO TUTORIAL -------
    #!/bin/sh
    export FLASK_APP=./cashman/index.py
    source $(pipenv --venv)/bin/activate
    flask run -h 0.0.0.0

    ------- NOVA SINTAXE -------
    #!/bin/sh
    export FLASK_APP=./flask_init/index.py
    source venv/scripts/activate
    flask run -h 0.0.0.0
    """
