

# Usuários criados durante e após a instalação
def contas():
    """
    chave: root                   valor: m***l*bu****in***s
    chave: luuk2772               valor: pa*****t*77*
    """


def fonte():
    """
    Curso || Banco de dados SQL e NoSQL - do básico ao avançado
    Seção || 6: MySQL - Parte 1
    Aula  || 45. Instalação e Configuração no Linux
    """


# Comandos de atualização no OS Ubuntu (antes de instalar o MySQL)
def parte1():
    """
    • sudo apt update && sudo apt -y upgrade && sudo apt list --upgradable
    • sudo reboot
    """


# Comando para instalar o servidor MySQL
def parte2():
    """
    • sudo apt install mysql-server
    • O instalador será iniciado (digitar Y e ENTER)
    """


# Comandos pós instalação do MySQL (verificar integridade da instalação)
def parte3():
    """
    ---------------------------------------------- COMANDOS RECOMENDADOS ----------------------------------------------
    • sudo mysql                    #  Logar no console MySQL
    • help                          #  Lista de comandos do console MySQL
    • exit                          #  Sair do console MySQL
    • sudo systemctl status mysql   #  Verificar status do servidor mysql pós sua instalação
    • sudo systemctl enable mysql   #  Iniciar servidor MySQL com o sistema operacional

    ---------------------------------- COMANDOS EXTRAS QUE SE DEVE SABER QUE EXISTEM ----------------------------------
    • sudo systemctl disable mysql  #  Cancelar iniciar o servidor MySQL com o sistema operacional
    • sudo systemctl start mysql    #  Iniciar/reiniciar servidor MySQL
    • sudo systemctl stop mysql     #  Congelar servidor MySQL
    """


# Configuração do servidor MySQL (criação da conta root)
def parte4():
    """
    • sudo mysql_secure_installation
    • É requisitado a criação da senha do usuário root
    • É requisitado se a senha deve ser mantida (aprovar com y/Y ou qualquer outra tecla para cancelar)
    • Remove anonymous users?                (y/Y)
    • Disallow root login remotely?          (y/Y)
    • Remove test database and access to it? (y/Y)
    • Reload privilege tables now?           (y/Y)
    """
