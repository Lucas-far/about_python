

# Configurar um arquivo git para ignorar arquivos de projeto de forma permanente (requer instalação do Git)
def parte_1():
    """
    ----------------------------------------------------- WINDOWS -----------------------------------------------------
    - Ir à pasta principal do usuário e criar um arquivo de texto [ .gitignore_global ]
    - Abrir o arquivo e inserir o conteúdo:

        .idea/
        bin/
        *.sqlite3

    - Abrir a pasta principal do usuário pelo terminal
    - git config --global core.excludesfile .gitignore_global

    ------------------------------------------------------ UBUNTU ------------------------------------------------------
    - Ir à pasta principal do usuário [ /home/seu_user/ ] e criar um arquivo de texto [ .gitignore_global ]
    - Abrir o arquivo e inserir o conteúdo:

        .idea/
        bin/
        *.sqlite3

    - Abrir a pasta principal do usuário pelo terminal
    - git config --global core.excludesfile ~/.gitignore_global
    """
