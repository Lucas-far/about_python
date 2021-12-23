

# Vincular arquivos locais (repositório local) com um repositório remoto (criado pelo Github)
def obs():
    """
    - Antes de fazer uma vinculação entre um [ repositório local ] com um [ repositório remoto ], é preciso haver
      conteúdo na pasta que representa um projeto p/ que o comando posterior [ git commit -m 'first commit' ] funcione

    - A adição de conteúdo pode ser qualquer arquivo criado na pasta do projeto, e como foi visto nas partes anteriores,
      dentro da pasta do projeto já há arquivos referentes ao [ ambiente virtual ]

    - Não deve ser esquecido que o ambiente virtual, além de estar INSTALADO, também deve estar ATIVADO

    - Os comandos para gerenciar ambientes virtuais foram mencionados na [ parte_3 ]
    """


# Como a configuração é direcionado para um repositório já com arquivos, então seguir o primeiro tutorial
def parte_4():
    """
    ------------------------------ CASO O REPOSITÓRIO LOCAL SEJA EXISTENTE (COM ARQUIVOS) ------------------------------
    1 - Ir ao site do Github e iniciar a criação de um repositório
    2 - Criar o repositório ignorando os arquivos de configuração [ README.MD ] [ .gitignore ] [ LICENSE ]
    3 - Copiar o link SSH que aparece após a criação do repositório

    git init
    git remote add origin link_ssh
    git add .
    git commit -m 'first commit' (aspas duplas se estiver no Windows e fazendo diretamente pelo terminal)
    git branch -M main
    git push -u origin main

    ---------------------------------------- CASO O REPOSITÓRIO LOCAL SEJA NOVO ----------------------------------------
    1 - Ir ao site do Github e iniciar a criação de um repositório
    2 - Criar o repositório adicionando os arquivos de configuração [ README.MD ] [ .gitignore ] [ LICENSE ]
    3 - Copiar o link SSH que aparece após a criação do repositório

    git init
    git add .
    git commit -m "first commit"
    git branch -M main
    git remote add origin link_ssh
    git push -u origin main
    """
