

def fonte():
    """
    Curso # Banco de dados SQL e NoSQL - do básico ao avançado
    Seção # Seção 8:PostgreSQL - Parte 1
    Aula  # 75. Instalação e Configuração no Linux
    """


# Comandos utilitários antes da instalação
def parte1():
    """
    sudo apt update && sudo apt -y upgrade && sudo apt list --upgradable
    sudo reboot
    """


# Download e procedimentos iniciais de instalação do PostgreSQL
def parte2():
    """
    1 - Download -> https://www.postgresql.org/download/linux/ubuntu/
    1 - sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
    2 - wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
    3 - sudo apt-get update
    4 - sudo apt-get -y install postgresql-13

    COMANDO QUE PODE APARECER DURANTE A INSTALAÇÃO:
    5 - pg_ctlcluster 13 main start
    """


# Comandos em caso haja problemas em relação a parte 2
def parte3():
    """
    Após os comandos anteriores, pode haver um erro de arquitetura [ i386 ]. Os códigos abaixo podem ajudar

    Se   [ dpkg --print-foreign-architectures ] == i386, então continuar
    Se   [ dpkg --print-architecture ]          == amd64, então continuar
    Usar [ sudo dpkg --remove-architecture i386 ]
    """


# Download da interface gráfica do PostgreSQL
def parte4():
    """ sudo apt-get -y install pgadmin4 """


# Comandos básicos relacionados os PostgreSQL
def parte5():
    """
    sudo su - postgres  # logar no postgresql com a conta padrão admin [ postgres ]
    psql                # usar o console psql em uma conta já logado [ no contexto: postgres ]
    help                # buscar comandos auxiliares
    \q                  # deslogar a conta
    exit                # deslogar do postgresql
    """
