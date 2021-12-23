

# Instalação do Python
def parte_2():
    """
    - Fazer o download, abrir o instalador, escolher a instalação padrão, e marcar [ add python to PATH ]
    - O resto da instalação deve ser mantida
    - Ao final da instalação, comandos de terminal devem ser feitos
    - Registrar binários nas variáveis de ambiente (Windows)

        C:\Users\seu_user\AppData\Local\Programs\Python\Python39\        ( interpretador do Python )
        C:\Users\seu_user\AppData\Local\Programs\Python\Python39\Scripts ( pip do Python )

    - No terminal, testar os comandos: [ python -V ] e [ pip -V ] para saber se o Python e Pip estão configurados
    - No terminal, digitar [ pip install --upgrade pip ]
    """


# 1 - Há duas formas (que eu conheço) de se criar ambientes virtuais
#     2 - Uma delas é natural do Python, pelo comando [ python -m venv nome_ambiente ]
#     3 - A outra forma é pela instalação de uma dependência, pelos comandos [ pip install virtualenv ]
#                                                                            [ pip install virtualenvwrapper-win ]
#
#     4 - O item 2 parece melhor, pois o ambiente é criado dentro do projeto
#         O item 3 requer instalação, e guarda ambientes craidos em uma pasta separada (pré-configurada)
#         O item 3 requer a configuração de uma variável de usuário
#
#             nome =  [ WORKON_HOME ] ou outro qualquer
#             valor = [ criar uma pasta 'Envs' na pasta do usuário e copiar o caminho da pasta 'Envs' para cá ]
#
#     5 - Antes de fazer uma vinculação entre um [ repositório local ] com um [ repositório remoto ], é preciso haver
#         conteúdo na pasta que representa um projeto p/ que o comando posterior [ git commit -m 'first commit' ] funcione
#
#     6 - A adição de conteúdo pode ser qualquer arquivo criado na pasta, mas é recomendável que este seja os arquivos
#         relacionados ao ambiente virtual
#
#     7 - Sendo assim, antes de qualquer vinculação entre repositórios, é melhor INSTALAR e ATIVAR um ambiente virtual
#
#     8 - Os comandos que seguem, devem ser feitos dentro da pasta do projeto, estando logada pelo terminal
#         Criar um ambiente virtual: [ python3 -m venv nome_ambiente            ] (Windows/Ubuntu) (item 2)
#         Criar um ambiente virtual: [ mkvirtualenv nome_ambiente               ] (Windows/Ubuntu) (item 3)
#         Ativar ambiente virtual:   [ nome_ambiente\scripts\activate           ] (Windows)        (item 2)
#         Ativar ambiente virtual:   [ source nome_ambiente/bin/activate        ] (Ubuntu)         (item 2)
#         Ativar ambiente virtual:   [ caminho_ambiente\scripts\activate        ] (Windows)        (item 3)
#         Ativar ambiente virtual:   [ source caminho_ambiente\scripts\activate ] (Windows)        (item 3)