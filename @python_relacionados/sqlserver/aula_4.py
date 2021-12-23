

def fonte():
    """
    SQL Server para Programadores/Desenvolvedores
    Seção 2: Setup
    4. Instalação do SQL Server - Linux em máquina virtual
    """


# Download do cliente
def parte_1():
    """
    Google || sql server linux download
    Título || Ubuntu: Instalar o SQl Server em Linux - Microsoft Docs
    Url    || https://docs.microsoft.com/pt-br/sql/linux/quickstart-install-connect-ubuntu?view=sql-server-ver15
    Info   || Na parte mais funda da página, procurar e clicar no botão de download referente à [ Desenvolvedor ]
    """


# Tutorial de instalação baseado no link fornecido acima
def parte_2():
    """
    Para instalar o Ubuntu 20.04 no seu computador, acesse
        https://releases.ubuntu.com/20.04/

    Também é possível criar máquinas virtuais Ubuntu no Azure
        https://docs.microsoft.com/pt-br/azure/virtual-machines/linux/tutorial-manage-vm

    Para obter outros requisitos do sistema
        https://docs.microsoft.com/pt-br/sql/linux/sql-server-linux-setup?view=sql-server-ver15#system

    ---------------------------------------------------- INSTALAÇÃO ----------------------------------------------------
    Para configurar o SQL Server no Ubuntu, execute os seguintes comandos em um terminal para instalar o pacote mssql-
    server.

    1. Importe as chaves GPG do repositório público:
        wget -qO- https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -

    2. Registre o repositório do Ubuntu do Microsoft SQL Server para o SQL Server 2019:

    Para o Ubuntu 16.04, 18.04, 20.04 respectivamente:

        sudo add-apt-repository "$(wget -qO- https://packages.microsoft.com/config/ubuntu/16.04/mssql-server-2019.list)"
        sudo add-apt-repository "$(wget -qO- https://packages.microsoft.com/config/ubuntu/18.04/mssql-server-2019.list)"
        sudo add-apt-repository "$(wget -qO- https://packages.microsoft.com/config/ubuntu/20.04/mssql-server-2019.list)"

    3. Execute os comandos a seguir para instalar o SQL Server:
        sudo apt-get update
        sudo apt-get install -y mssql-server

    4. Após a conclusão da instalação do pacote, execute a instalação de mssql-conf e siga os prompts para definir a
    senha SA e escolher sua edição.

        sudo /opt/mssql/bin/mssql-conf setup

    ---------------------------------------------------- INSTALAÇÃO ----------------------------------------------------
    Choose an edition of SQL Server: [ Developer (free, no production use rights) ]
    Do you accept the license terms? [ Digitar Yes ]

        OBS: Especifique uma senha forte para a conta SA (comprimento mínimo de 8 caracteres, incluindo letras
             maiúsculas e minúsculas, 10 dígitos básicos e/ou símbolos não alfanuméricos).

    5. Após concluir a configuração, verifique se o serviço está em execução:
        systemctl status mssql-server --no-pager

        Ao executar o comando acima, verifique se há [ active (running) ]
    """


# Informações de instalação extras
def parte_3():
    """
    ---------------------------- Instalar as ferramentas de linha de comando do SQL Server ----------------------------
    1. Por padrão, o curl não é instalado no Ubuntu. Para instalar o curl, execute este código:
        sudo apt-get update
        sudo apt install curl

    2. Importe as chaves GPG do repositório público.
        curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -

        Nessa etapa, é provável a aceitação de termos, usar [ Yes ] para todos

    3. --------------------------------------------------- Opcional ---------------------------------------------------
    - Adicione /opt/mssql-tools/bin/ à sua variável de ambiente PATH em um shell de Bash.

    - Para tornar o sqlcmd/bcp acessível do shell de Bash para sessões de logon, modifique o PATH no arquivo
      [ ~/.bash_profile ] com o seguinte comando:

      echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile

    - Para tornar o sqlcmd/bcp acessível do shell de Bash para sessões interativas/que não são de logon, modifique o
      PATH no arquivo ~/.bashrc com o seguinte comando:

      echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc source ~/.bashrc
    """
