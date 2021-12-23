

# Tipos de conexões possíveis do SQL Server pelo computador
def parte_1():
    """
    Pelo windows || Nome da máquina, localhost, ip da máquina
    Pelo Ubuntu  || ip da máquina
    """


# Instalação do SQL Server e dados ao final da instalação
def parte_2():
    """
    A instalação é genérica, não precisando qualquer configuração diferenciada

    1. Nome da instância   || MYSQLSERVER
    2. Administradores SQL || DESKTOP-LD4QVe6\lucasf
    3. Recursos instalados || SQLENGINE
    4. Versão              || 15.0.2000.5, RTM
    5. Cadeia de conexão   || Server=localhost;Database=master;Trusted_Connection=True;
    6. Pasta de log        || C:\Program Files\Microsoft SQL Server\150\Setup Bootstrap\Log\20211222_112139
    7. Pasta de mídia      || C:\SQL2019\Developer_PTB
    8. Pasta de recursos   || C:\Program Files\Microsoft SQL Server\150\SSEI\Resources
    """


# Configuração do SQL Server Configuration Manager
def parte_3():
    """
    1. Abrir o software
    2. No painel à esquerda, acessar [Configuração de rede do SQL server]
    3. No painel à esquerda, acessar [Protocolos para MYSQLSERVER]
    4. Habilitar [Pipes nomeados] e [TCP/IP]

    5. Acessar [Configuração do SQL native client] e [Protocolos de rede]
    OBS: No item 5, há duas versões, a de 32 e 64 bits (fazer em ambas, caso não estejam já configuradas)
    6. As opções nessa configuração devem estar todas habilitadas
    """


# Configuração do SQL Server Management Studio
def parte_4():
    """
    ----- TERMINAL -----
    1. Essa parte têm relação direta com o que foi dito na [parte_1]
    2. A configuração será pelo nome da máquina (outras formas foram mostradas nessa aula: 5)
    3. Abrir o terminal, digitar [hostname] e copiar o retorno

    ------- TELA DE ENTRADA -------
    4. Abrir o SQL Server Management Studio, que ao ser aberto pela primeira vez, requisitará uma conexão
    5. Inserir o hostname no campo vazio na tela
    6. A conexão não deve ter problemas se a [parte_3] tiver sido feita

    ------- TELA PRINCIPAL -------
    7. No painel à esquerda, botão direito sob o nome da instância e selecionar [Propriedades]
    8. No painel à esquerda, clicar em [Segurança] e marcar [Modo de autenticação do Sql server e Windows]

    ------- CONFIGURAÇÃO EXTRA ------- (motivo não explicado)
    9. A configuração têm haver com um [super usuário=sa] e é uma configuração feita apenas no modo desenvolvedor
    10. Na outra versão do SQL Server [produção], essa configuração não é feita
    11. No painel principal: [Segurança/Logons] e acessar as propriedades do usuário [sa]
    12. Desmarcar a opção [Impor política de senha], inserir uma senha menor
    13. Ainda no usuário, clicar na opção [Status] no painel esquerdo, e habilitar a opção de logon
    14. Outros procedimentos foram feitos (assistir aula 5, a partir de 09:00)
    """
