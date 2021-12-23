

# Criação do usuário novo apartir do MySQL Monitor
def parte_1():
    """
    ----------------------------------------------------- DETALHE -----------------------------------------------------
    • A criação de um usuário novo pode conter dificuldades, devido a política de criação de senha do MySQL
    • Isso pode ser mudado, através dos itens 2 e 3
    • Retorno comum de erro caso os itens 2 e 3 não seja configurados
        ERROR 1819 (HY000): Your password does not satisfy the current policy requirements

    ------------------------------------------------ CRIAÇÃO DO USUÁRIO ------------------------------------------------
    1 • sudo mysql
    2 • SHOW VARIABLES LIKE 'validate_password%';
    3 • SET GLOBAL validate_password.policy=LOW;
    4 • CREATE USER 'nome do usuário'@'localhost' IDENTIFIED BY 'senha desejada';
    5 • GRANT ALL PRIVILEGES ON *.* TO 'usuário criado'@'localhost' WITH GRANT OPTION;
    6 • FLUSH PRIVILEGES;
    7 • exit
    8 • sudo mysql -u nome do usuário novo -p
    9 • digitar a senha do usuário novo
    """


# Comandos pós criação login de uma conta (apenas para informação)
def parte_2():
    """
    SHOW DATABASES;                  # Mostrar todos os bdds
    USE nome do bdd;                 # Acessar um bdd específico (se você está em outro bdd, ele será deslogado)
    SHOW TABLES;                     # Mostrar tabelas de um bdd (já estando logado em um bdd específico)
    SELECT * FROM tabela de um bdd;  # Consultar uma tabela específica
    SELECT * FROM sys_config;        # Exemplo do comando acima
    """


# Download e instalação do MySQL Workbench
def parte_3():
    """
    ------------------------------------------------------ FONTE ------------------------------------------------------
    Curso || Banco de Dados SQL e NoSQL do básico ao avançado (Udemy)
    Seção || 3: Modelagem de Dados
    Aula  || 18. Download, Instalação e Configuração do MySQL Workbench no Linux

    ----------------------------------------------------- PESQUISA -----------------------------------------------------
    • Google      || Mysql workbench ubuntu download
    • Resultado   || Download MySQL Workbench
    • Link direto || https://dev.mysql.com/downloads/workbench/
    • É preciso selecionar o SO para download

    ------------------------------------------- PROCEDIMENTOS DE INSTALAÇÃO -------------------------------------------
    • O instalador no Ubuntu é similar ao do Windows, podendo ser instalado de forma direta, sem códigos
    • Ao final da instalação, verificar se o software está visível em 'SHOW APPLICATIONS'
    """
