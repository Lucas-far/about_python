

"""
Módulo: instalar_nodejs_ubuntu.py.py
Palavra chave: node ubuntu

Curso || Curso Web Moderno Completo com JavaScript 2020 + Projetos
Seção || Seção 2:Configuração do Ambiente
Aula  ||
"""

# Instalação
"14.x"  # versão LTS mais atual do node de acordo com https://nodejs.org/en/
"5"     # Precisa haver a retorno da versão no terminal, para confirmar a instalação do NodeJS com sucesso
def parte1():
    """
    1 - sudo apt-get install curl
    2 - curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
    3 - sudo apt-get install -y nodejs
    4 - reiniciar o terminal
    5 - node --version
    6 - npm --version

    OUTROS COMANDOS TALVEZ RECOMENDÁVEIS:
        - sudo apt-get install gcc g++ make
        - curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
        - echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
        - sudo apt-get update && sudo apt-get install yarn
    """
