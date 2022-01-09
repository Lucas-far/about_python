

def fonte():
    """
    SQL Server para Programadores/Desenvolvedores
    Seção 2: Setup
    5. Instalação do SQL Server Management Studio
    """


# [ SQL Management Studio ] (download) (interface/ferramenta que faz o uso das instâncias de servidor)
def parte_1():
    """
    Google || sql management studio download
    Título || Baixar o SQL Server Management Studio (SSMS) - Microsoft...
    Url    || https://docs.microsoft.com/pt-br/sql/linux/quickstart-install-connect-ubuntu?view=sql-server-ver15
    Info   || Descendo um pouco a página, há um link [  Baixar o SQL Server Management Studio (SSMS) ]. Clique nele
    Info 2 || No próprio instalador do [ SQL Server ] há um botão para instalar chamado [ Instalar o SSMS ]
    """


# [ SQL Management Studio ] (instalação) (requer reiniciação)
def parte_2():
    """
    Local padrão: C:\Program Files (x86)\Microsoft SQL Server Management Studio 18 -> Install
    """


# [ SQL server configuration manager ] (verificação se o servidor encontra-se habilitado)
def parte_3():
    """
    - Após reiniciar, na janela do Windows, procurar por [ SQL server configuration manager ]
    - Abrir o software [ SQL server configuration manager ] como administrador
    - Na abertura, no painel esquerdo, em [ SQL Server Configuration Manager (Local) ] há opções
    - Selecionar [ Serviços do SQL Server ]
    - Se o [ SQL Server ] tiver o estado [ Em execução ], então tudo OK
    """


# [ Microsoft SQL Server Management Studio ] (configuração)
def parte_4():
    """
    - Abrir o software [ Microsoft SQL Server Management Studio ] como administrador (evitar erro 18456)
    - Na primeira abertura (após a instalação e reiniciação) é pedido uma configuração
    - A janela de [ Connect to Server ] abrirá. Deixe as coisas como estão e clique em [ Connect ]
    - No painel esquerdo, deverá ser aberto um servidor com o nome dado ao seu PC (item verde)
    - Botão direito no PC do painel -> Properties -> Security -> SQL Server and Windows Authentication mode (marcar) ->
      OK -> OK

    - Ir ao painel esquerdo, na linha [ Connect ], clicar no ícone [ tomada com X ] para disconectar (ñ precisa fechar)
    """


# [ SQL server configuration manager ] (configuração)
def parte_5():
    """
    - Abrir o software [ SQL server configuration manager ] como administrador
    - Ir pelo caminho [ Configuração de rede do SQL server ] [ Protocolos para MYSQLSERVER ] e habilitar todos
    - Ir pelo caminho [ Configuração do SQL Native Client ] [ Protocolos de cliente ] (todos devem estar habilitados)

    ----------------------------------------------------- DETALHE -----------------------------------------------------
    A última instrução pode ter mais de uma opção repetida, caso sim, verificar em todas as instâncias

    - Ir pelo caminho [ Serviços do SQL server ] [ botão direito no SQL Server ] [ reiniciar ]
    """


# [ Microsoft SQL Server Management Studio ] (+ configuração)
def parte_6():
    """
    - Na parte 4, ele foi aberto, e a última instrução foi desconectar o servidor
    - Ir ao painel esquerdo, na linha [ Connect ], clicar no ícone [ tomada ] para habilitar o servidor
    - Botão direito no PC do painel -> Properties -> Security
                                                     SQL Server and Windows Authentication mode (verificar marcação)

    - Ir pelo caminho [ Security ] [ Logins ] [ sa (botão ->) properties ]
    - Modificar os campos [ Password ] [ Confirm password ] [ OK ]
    - Ir pelo caminho [ Security ] [ Logins ] [ sa (botão ->) properties ] [ status (painel superior esquerdo) ]
    - No painel de [ status ] na opção [ Login ], marcar [ Enabled ]
    - Deslogar do servidor pelo ícone [ tomada X ] e relogar pelo ícone [ tomada ]
    - Ir pelo caminho [ Security ] [ Logins ] e note que o [ sa ] está [ ativado ]
    - Deslogar novamente, e relogar, mas dessa vez será pelo [ sa ]

    --------------------------------------------- LOGIN PELO SUPER USUÁRIO ---------------------------------------------
    - As etapas a seguir foram mostradas pelo professor, mas mostraram [ Microsoft SQL Server error 233 ]

    - No painel [ Server name=localhost ] [ Authentication=SQL server authentication ]
    - No painel [ Login=sa ] [ Password=senha definida nas configurações anteriores ]

    - No painel [ Server name=ipv4 (ipconfig) ] [ Authentication=SQL server authentication ]
    - No painel [ Login=sa ] [ Password=senha definida nas configurações anteriores ]

    - Eu consegui somente pela forma padrão
    - No painel [ Server name=nome da máquina ] [ Authentication=Windows authentication ]
    """


# [ Microsoft SQL Server Management Studio ] (criar usuário)
def parte_7():
    """
    - Ir pelo caminho [ Security ] [ Logins (botão ->) ] [ New login... ]
    - [ Login name=nome_subjetivo ] [ SQL server authentication (marcar) ]
    - [ Password=subjetivo ] [ Confirm password=subjetivo ] [ enforce password policy (desmarcar) ] [ OK ]
    """


# [ Microsoft SQL Server Management Studio ] (criar bdd) (vincular bdd)
def parte_8():
    """
    - Ir pelo caminho [Databases (botão ->) ] [ New database... ] [ Database name=subjetivo ] [ OK ]

    ------------------------------------------ VINCULAÇÃO DO BANCO AO USUÁRIO ------------------------------------------
    - Ir pelo caminho [ Security ] [ Logins ] [ clicar no usuário (botão ->) ] [ properties ]
                      [ default database=nome do bdd criado acima (fundo esquerdo da tela) ] [ OK ]
    """


# E-trade problema (ligar base) (sql network interfaces error 26)
def problema():
    """
    - Abrir [ SQL server configuration manager ] [ Serviços do SQL server ] [ SQL server browser ] [ botão -> ]
            [ propriedades ] [ serviço ] [ modo inicial=manual/automático ] [ Aplicar & OK ]
            [ Serviços do SQL server ] [ SQL server browser ] [ botão -> ] [ iniciar ]

    - Abrir [ painel de controle ] [ sistema e segurança ] [ windows defender firewall ] [ configurações avançadas ]
            [ regras de entrada (clicar) ] [ nove regra (canto superior esquerdo) ] [ port ]
            [ todas as portas ] [ permitir a conexão ] [ avançar ] [ nome=subjetivo ]

    - Após criar a regra, selecionar ela [ botão -> ] [ propriedades ] [ protocolos e portas ]
                                         [ tipo de protocolo=qualquer ] [ aplicar & OK ]

    - Abrir [ SQL server configuration manager ] [ Configuração de rede do SQL server ] [ Protocolos para MYSQLSERVER ]
            [ TCP/IP ] [ duplo clique=propriedades ] [ Endereços IP ] [ Habilitado=sim ] [ aplicar & OK ]

    - No [ SQL server configuration manager ] [ Serviços SQL server ] [ SQL Server (botão ->) ] [ reiniciar ]
    """