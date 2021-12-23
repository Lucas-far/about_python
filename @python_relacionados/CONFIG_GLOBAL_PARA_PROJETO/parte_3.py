

# Criação da pasta do projeto e ambiente virtual
def parte_3_com_dependencia():
    """
    - pip install virtualenv
    - pip install virtualenvwrapper-win

    - É opcional caso queira criar ambientes virtuais ISOLADOS dos seus projetos
    - Requer a configuração de uma variável de usuário

        CONFIGURAÇÃO DA VARIÁVEL
            nome =  [ WORKON_HOME ] ou outro qualquer
            valor = [ criar uma pasta 'Envs' na pasta do usuário e copiar o caminho da pasta 'Envs' para cá ]

    - Para verificar se a variável funciona corretamente, fazer no terminal o comando [ echo %NOME_VARIÁVEL% ]
    - Criar uma pasta no diretório do usuário (nome é subjetivo)
    - Entrar nessa pasta pelo terminal

    COMANDOS RELACIONADOS AOS AMBIENTES VIRTUAIS (estando da pasta do projeto pelo terminal)
        mkvirtualenv nome_ambiente   # criação e login em um ambiente
        deactivate                   # deslogar de um ambiente
        workon nome_ambiente         # relogar em um ambiente criado
        rmvirtualenv nome do av      # remover um ambiente especificado
    """


def parte_3_sem_dependencia():
    """
    - Criar uma pasta no diretório do usuário (nome é subjetivo)
    - Entrar nessa pasta pelo terminal
    - python -m venv nome_ambiente      (criação do ambiente e login automático) (Windows & Ubuntu)
    - deactivate                        (deslogar do ambiente)                   (Windows & Ubuntu)
    - nome_ambiente\scripts\activate    (relogar no ambiente)                    (Windows)
    - source nome_ambiente/bin/activate (relogar no ambiente)                    (Ubuntu)
    - o ambiente pode ser deletado como qualquer arquivo
    """
