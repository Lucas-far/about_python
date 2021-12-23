

# Procedimentos não mandatórios que recomenda-se saber (após instalar o GIT)
def obs():
    """
    git config --global user.name "seu_user"      git config user.name (verificar)
    git config --global user.email "seu_email"    git config user.email (verificar)
    git config --list                             verificar outros comandos GIT
    """


# Este procedimento necessita uma chave ssh criada e vinculada a sua conta Github [ criar_chave_ssh_windows.py ]
def parte_1():
    """
    Ler este tópico abaixo antes de qualquer coisa

    ------------------------------------------------ PROCEDIMENTO ÚTIL ------------------------------------------------
    1 - Há duas formas (que eu conheço) de se criar ambientes virtuais
    2 - Uma delas é natural do Python, pelo comando [ python -m venv nome_ambiente ]
    3 - A outra forma é pela instalação de uma dependência, pelos comandos [ pip install virtualenv ]
                                                                           [ pip install virtualenvwrapper-win ]

    4 - O item 2 parece melhor, pois o ambiente é criado dentro do projeto
        O item 3 requer instalação, e guarda ambientes craidos em uma pasta separada (pré-configurada)
        O item 3 requer a configuração de uma variável de usuário

            nome =  [ WORKON_HOME ] ou outro qualquer
            valor = [ criar uma pasta 'Envs' na pasta do usuário e copiar o caminho da pasta 'Envs' para cá ]

    5 - Antes de fazer uma vinculação entre um [ repositório local ] com um [ repositório remoto ], é preciso haver
        conteúdo na pasta que representa um projeto p/ que o comando posterior [ git commit -m 'first commit' ] funcione

    6 - A adição de conteúdo pode ser qualquer arquivo criado na pasta, mas é recomendável que este seja os arquivos
        relacionados ao ambiente virtual

    7 - Sendo assim, antes de qualquer vinculação entre repositórios, é melhor INSTALAR e ATIVAR um ambiente virtual

    8 - Os comandos que seguem, devem ser feitos dentro da pasta do projeto, estando logada pelo terminal
        Criar um ambiente virtual: [ python3 -m venv nome_ambiente            ] (Windows/Ubuntu) (item 2)
        Criar um ambiente virtual: [ mkvirtualenv nome_ambiente               ] (Windows/Ubuntu) (item 3)
        Ativar ambiente virtual:   [ nome_ambiente\scripts\activate           ] (Windows)        (item 2)
        Ativar ambiente virtual:   [ source nome_ambiente/bin/activate        ] (Ubuntu)         (item 2)
        Ativar ambiente virtual:   [ caminho_ambiente\scripts\activate        ] (Windows)        (item 3)
        Ativar ambiente virtual:   [ source caminho_ambiente\scripts\activate ] (Windows)        (item 3)

    ------------------------------ CASO O REPOSITÓRIO LOCAL SEJA EXISTENTE (COM ARQUIVOS) ------------------------------
    1 - Criar o repositório ignorando os arquivos de configuração [ README.MD ] [ .gitignore ] [ LICENSE ]
    2 - Copiar o link SSH que aparece após a criação do repositório

    git init
    git remote add origin link_ssh
    git add .
    git commit -m 'first commit'
    git branch -M main
    git push -u origin main

    ---------------------------------------- CASO O REPOSITÓRIO LOCAL SEJA NOVO ----------------------------------------
    1- Criar o repositório adicionando os arquivos de configuração [ README.MD ] [ .gitignore ] [ LICENSE ]

    git init
    git add .
    git commit -m "first commit"
    git branch -M main
    git remote add origin link_ssh
    git push -u origin main
    """
