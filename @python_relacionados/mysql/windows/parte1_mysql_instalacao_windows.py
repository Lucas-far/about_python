

# Necessária para fazer o download
def contas():
    """
    chave: lu____ei2@gmail.com    valor: W***p*s*1*
    chave: root                   valor: m***l*bu****in***s
    chave: luuk2772               valor: pa*****t*77*
    chave: luuk2772_2nd           valor: pa*****t*77*_***
    """


# Gerenciamento da instalação do MySQL
def parte_2():
    """
    ----------------------------------------------------- Tutorial -----------------------------------------------------
    • Procurar no google por [ mysql windows ] ou ir á página [ https://www.mysql.com/ ]
    • Ir à aba de downloads [ https://www.mysql.com/downloads/ ]
    • Procurar pelo link [ MySQL Community (GPL) Downloads ] (link no fundo e centro da página)
    • Procurar pelo link [ MySQL Community Server ] [ https://dev.mysql.com/downloads/mysql/ ]
    • Clicar em [ go to download page ] = [ https://dev.mysql.com/downloads/windows/installer/8.0.html ]
    • Fazer o download do instalador [ Windows (x86, 32-bit), MSI Installer ]

    OBS: Para efetuar o download é preciso logar numa conta Oracle e preencher um pequeno formulário

    ---------------------------------------------------- Problemas ----------------------------------------------------
    • O instalador no Windows possui problemas de carregamento
    • Abrir o Gerenciador de Tarefas como admin
    • Iniciar o instalador, e caso há problemas de progresso, fechar a tarefa 'Windows Installer 32 bits'
    • É provável que ao fazer isso, o instalador começe a funcionar
    """


# Problemas com usuário 'ROOT' que não pode ser criado, mesmo após desinstalação e reinstalação
def problema_escroto():
    """
    Abrir o instalador e desinstalar todas as ferramentas (não desinstalar o instalador)
    Remover a pasta do MySQL nesse caminho [ C:\Users\seu_user\AppData\Roaming ]
    Remover a pasta do MySQL nesse caminho [ C:\ProgramData\MySQL ] [ pasta precisa ser configurada para ser vista ]
    Remover a pasta do MySQL nesse caminho [ C:\Program Files\MySQL ]
    Reiniciar o PC e tentar instalar normalmente
    """


# Setup do MySQL (Porta MySQL = 3306)
def parte_3():
    """
    ------------------------------------------ SETUP PARA PRIMEIRA INSTALAÇÃO ------------------------------------------
    • Choosing a Setup Type || Custom -> [ next ]

    SOFTWARES A SEREM INSTALADOS
    • Select Products || MySQl Servers -> MySQL Server -> MySQL Server 8.0 -> MySQL Server 8.0.26 - X64
    • Select Products || Applications -> MySQL Workbench -> MySQL Workbench 8.0 -> MySQL Workbench 8.0.26 - x64
    • Select Products || MySQL Connectors -> Connector/Python -> Connector/Python 8.0 -> Connector/Python 8.0.26 - X64
    • [ next ]

    • Installation || MySQl Server 8.0.26 -> MySQL Workbench 8.0.26 -> Connector/Python 8.0.26 -> [ execute ]
    • Installation || O download das ferramentas será feito, após completar todos, clica-se em [ next ]

    • Product Configuration || [ next ]
    • Type and Networking   || [ next ]
    • Authentication Method || Use Strong Password Encryption -> [ next ]

    • Accounts and Roles    || Configuração do usuário matriz [ nome = root ] -> configurar senha -> [ next ]
                               Existe um botão [ Add User ] para inserir usuários principais além do [ root ]

    • Windows Service       || [ next ]
    • Apply Configuration   || [ execute ]
    • Product Configuration || [ next ]
    • Instalation Complete  || [ finish ]

    OPÇÃO DESCONTINUADA
    Group Replication     || Standalone MySQL Server / Classic MySQL Replication -> [ next ]

    ----------------------------------------- SETUP PARA INSTALAÇÃO EXISTENTE -----------------------------------------
    Check and Upgrade Database -> [ next ]
    Apply Configuration -> [ execute ]
    """


# Configuração do path do MySQL
def parte_4():
    """
    • O caminho normal de instalação do MySQL é [ C:\Program Files\MySQL ]
    • Passando por mais duas pastas específicas, o caminho muda para [ C:\Program Files\MySQL\MySQL Server 8.0\bin ]
    • Copiar essa caminho, pois será usado logo abaixo

    ---------------------------------------- ADICIONAR MySQL AO PATH DO WINDOWS ----------------------------------------
    • Win     • Este computador    • Configurações avançadas do sistema
    • Propriedades do sistema -> [ Variáveis de ambiente ]
    • Variáveis de Ambiente -> Variáveis do sistema -> Path (marcar) -> [ editar ]
    • Editar a variável de ambiente -> [ novo ] -> ctrl + V -> ENTER -> OK -> OK
    """


# Primeiro acesso ao MySQL (teste de login do usuário matriz e da abertura do MySQL monitor)
def parte_5():
    """
    • mysql -u root -p
    • Inserir a senha configurado na instalação
    • Se os dados estiverem certos, será aberto o [ MySQL monitor ]

    ----------------------------------------------- COMANDOS RELEVANTES -----------------------------------------------
    MySQL Monitor (lista de comandos) [ help ]
    MySQL Monitor (fazer logout)      [ exit ] [ \q; ]
    """


# Comandos de usuário logado
def parte7():
    """
    SHOW DATABASES;                || Mostrar uma lista de todos os bdds disponíveis de um usuário logado
    USE nome do bdd;               || Logar em um dos bdds disponíveis de um usuário logado
    SHOW TABLES;                   || Mostrar todas as tabelas criados de um bdd alvo de um usuário logado
    SELECT * FROM nome da tabela;  || Mostrar tabelas das tabelas de um bdd alvo de um usuário logado
    """
