

"""
Módulo ### instalar_python_ubuntu.py

Palavra chave: instalar python ubuntu
"""

# Softwares: 1. Java development kit (oracle) / 2. Python / 3. Pycharm
def softwares():
    """
    1. 04-jdk-11.0.7_linux-x64_bin.tar.gz
       FONTES:
              Google = Java Archive Downloads - Java SE 11 - Oracle
              https://www.oracle.com/java/technologies/javase/jdk11-archive-downloads.html

    2. python-3.8.5.tar.xz
       FONTES:
              https://www.python.org/downloads/ (Site / Downloads / All releases)

    3. pycharm-community-2020.2.tar.gz
    4. CONTA ORACLE: [ lu******2@g****.com ] [ W******s17 ]
    """

def configurar_java():
    """
    1. Extrair o módulo compilado java baixado no mesmo local onde ele está [ Extract here ]
    2. Renomear o diretório para [ jdk11 ]
    3. Se em [ jdk11 ] há módulos aninhados, leve todos para o diretório matriz
    4. Recortar (ctrl + x) o diretório [ jdk11 ]
    5. /home/meu_user/apps (se não existe, criar este diretório)
    6. Colar (ctrl + v) o diretório [ jdk11 ] em /home/meu_user/apps
    7. Retornar um nível [ /home/meu_user ]
    8. ctrl + h (para mostrar módulos ocultos)
    9. Procurar e abrir [ .bashrc ]
    10. Vá ao final do módulo e adicione as seguintes linhas de código:

        JAVA_HOME=/home/meu_user/apps/jdk11
        export JAVA_HOME
        PATH=$PATH:$JAVA_HOME/bin
        export PATH

    11. Ir ao terminal, e checar se o Java foi instalado: [ java --version ]
    12. Se há um retorno da versão do Java, então teve sucesso
    """

# Atualizam-se os pacotes do Ubuntu
def terminal():
    """ sudo apt-get update """

# Ferramentas essenciais
def terminal2():
    """
    sudo apt-get install -y build-essential aria2 blt-dev curl gettext git libbz2-dev libffi-dev libgdbm-dev libjpeg-dev liblzma-dev libncurses5-dev libnss3-tools libreadline-dev libsqlite3-dev libssl-dev llvm python-dev python3-dev python3-venv sqlite3 tcl-dev tk-dev vim wget zlib1g-dev
    """

def configurar_python():
    """
    1 - Extrair o módulo compilado python baixado no mesmo local onde ele está [ Extract here ]
    2 - Entrar na pasta extraida do Python
    3 - botão direito >>> open in terminal
    4 - ./configure --enable-optimizations --with-ensurepip=install
    5 - make -j 2
    6 - sudo make altinstall
    7 - python 3 --version / python3.8 --version
    8 - pip3.8 --version
    9 - sudo pip3.8 install --upgrade pip
    """

# Ferramenta para Python
def virtualenv():
    """
    1 - sudo pip3.8 install virtualenv virtualenvwrapper
    2 - Ir a rota [ /home/meu_user ]
    3 - ctrl + h (para mostrar módulos ocultos)
    4 - Procurar e abrir [ .bashrc ]
    5 - Vá ao final do módulo e adicione as seguintes linhas de código:

        export WORKON_HOME=$HOME/.virtualenvs
        export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3.8  # terminal: which python3.8
        source /usr/local/bin/virtualenvwrapper.sh

    6 - Ao fazer a configuração acima, está sendo configurada uma rota: [ /home/lucas/.virtualenvs ]
    7 - Nessa rota, podem ser criados ambientes virtuais baseando-se nos seguintes comandos:

        mkvirtualenv nome do av   # criação e login em um av
        deactivate                # deslogar de um av criado
        work on nome do av        # relogar em um av criado
        rmvirtualenv nome do av   # remover um av especificado

    8 - Ambientes virtuais criados nessa rota, já são ativados no terminal automaticamente
    9 - Mas e se for preciso fazer isso manualmente?

        9.1 - Supondo que haja um ambiente virtual em: [ /home/lucas/.virtualenvs/ ]
        9.2 - É preciso chegar até ele (pelo terminal)
        9.3 - Portanto, é preciso ir até ao diretório onde estão guardados os ambientes virtuais
        9.4 - ctrl + alt + T / cd .virtualenvs
        9.5 - ls (para ver os nomes das pastas dos ambientes existentes)
        9.6 - Agora, sabendo o nome do ambiente virtual, ele já pode ser ativado
        9.7 - Supondo que o nome do ambiente virtual seja: [ z ]
        9.8 - source z/bin/activate (para ativar)
        9.9 - source z/bin/deactivate (para desativar)

    10 - Porém, e se for desejado criar um ambiente virtual isolado da pasta matriz de criação?

         10.1 - Ir ao diretório desejado
         10.2 - Criar um diretório [ ex: pasta ]
         10.3 - Percorrer o diretório pelo terminal ou entrar na pasta manualmente: [ open in terminal ]
         10.4 - No terminal da rota da pasta, fazer: [ python3 -m venv venvpy3 ]
         10.5 - [ venvpy3 ] = nome do diretório onde o ambiente virtual será criado
         10.6 - Ao fazer isso, o ambiente virtual é criado, mas não é ativado
         10.7 - Para ativar: [ source venvpy3/bin/activate ]
         10.8 - Estando ativado, para desativar: [ deactivate ]
         10.9 - Não foi informado como deletar um ambiente virtual, então pode ser optado deletar manualmente
    """

# Ferramenta para Python
def pyenv():
    """
    1 - curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
    2 - Ir à rota: [ /home/seu_user/.bashrc ]
    3 - Abrir o módulo
    4 - Inserir no final do módulo:
                                   export PATH="/home/lucas/.pyenv/bin:$PATH"
                                   eval "$(pyenv init -)"
                                   eval "$(pyenv virtualenv-init -)"
    5 - Salvar
    6 - Fechar o terminal
    7 - Reabrir o terminal
    8 - pyenv
    9 - Se a instalação teve êxito, o Pyenv será chamado no terminal
    10 - pyenv install -l
    11 - Procurar na listagem, a versão inteiramente numérica mais atual
        EXEMPLO:
                3.9.1
    12 - pyenv install 3.9.1
    """

def configurar_pycharm():
    """
    1. Extrair o módulo compilado pycharm baixado no mesmo local onde ele está [ Extract here ]
    2. Renomear o diretório para [ pycharm ]
    3. /home/meu_user/apps (se não existe, criar este diretório)
    4. Recortar (ctrl + x) o diretório [ pycharm ] para [ /home/meu_user/apps/ ]
    5. Entrar no diretório [ pycharm/bin ]
    6. botão direito >>> open in terminal

    7. TERMINAL:
                sudo apt-get install alacarte -y

    8. Agora é melhor que seja configurado um ícone para o software, para melhor acesso
    9. Ir ao Desktop, em [ Show applications ]
    10. Procurar e abrir [ Main Menu ]
    11. [ Applications / Programming ]
    12. [ New item ] [ Name: Pycharm ] [ Command: /home/apps/pycharm/bin/pycharm.sh ]
    13. Adicionar um ícone: [ /home/lucas/apps/pycharm/bin/pycharm.png ]
    """

# Configuração essencial para criar projetos no Pycharm
def pycharm():
    """
    1. Abrir o software
    2. Clicar em [ New Project ]
    3. Há duas formas de criar um projeto novo

       FORMA 1: Quando um ambiente não foi criado usando o comando: [ mkvirtualenv ]

       1. Location = rota/nome do av
       2. New environment
              Base Interpreter
                  ...
                      /usr/local/bin/python3.8

       FORMA 2: Quando um ambiente já foi criado usando o comando: [ mkvirtualenv ]

       1. Location = rota/nome do av
       2. Existing Interpreter
              ...
                  Add Python Interpreter
                      /usr/bin/python3.8
    """
