

# Necessária para fazer o download
def contas():
    """
    chave: lu____ei2@gmail.com    valor: W***p*s*1*
    chave: postgres               valor: p********l*bntwi*
    chave: luuk2772               valor: pa*****t*77*
    chave: luuk2772_2nd           valor: pa*****t*77*_***
    """


# Download do Instalador
def parte_1():
    """
    • Ir ao website [ https://www.postgresql.org/ ], clicar na aba [ download ] e no botão referente ao [ windows ]
    • A página fornecerá um link, procure por ele [ nome visto na época = Download the installer ]
    • A página mudará para outro website, escolher a versão mais atual e a plafatorma [ Windows x86-64 ]
    • [ Download ]
    """


# Setup do instalador (Porta = 5432) (Arquivos salvos em C:\Program Files\PostgreSQL\14\data)
def parte_2():
    """
    • O instalador informa onde irá instalar o software, sendo o padrão [ C:\Program Files\PostgreSQL\ ]
    • Select Components || PostgreSQL Server -> pgAdmin4 -> Stack Builder -> Command Line Tools -> [ next ]
    • Data Directory    || Por padrão, o instalar recomenda [ C:\Program Files\PostgreSQL\13\data ] -> [ next ]
    • Password          || Escolher a senha e redigitar -> [ next ]
    • Port              || [ next ]
    • Advanced Options  || [ next ]

    • Pre Installation Summary || [ next ]
    • Ready to Install         || [ next ]
    • Installing               || procedimento demorado, pois o software é robusto
    • [ Finish ]
    """


# Configuração do path do PostgreSQL
def parte_4():
    """
    • O caminho normal de instalação do PostgreSQL é [ C:\Program Files\PostgreSQL ]
    • Passando por mais duas pastas específicas, o caminho muda para [ C:\Program Files\PostgreSQL\13\bin ]
    • Copiar essa caminho, pois será usado logo abaixo

    ---------------------------------------- ADICIONAR MySQL AO PATH DO WINDOWS ----------------------------------------
    • Win     • Este computador    • Configurações avançadas do sistema
    • Propriedades do sistema -> [ Variáveis de ambiente ]
    • Variáveis de Ambiente -> Variáveis do sistema -> Path (marcar) -> [ editar ]
    • Editar a variável de ambiente -> [ novo ] -> ctrl + V -> ENTER -> OK -> OK
    """


# Testar se o PostgreSQL foi configurado com sucesso
def parte_5():
    """
    • psql -U postgres
    • Inserir a senha do usuário admin [ postgres ] configurada durante a instalação
    • Se tudo foi feito corretamente, o terminal retornará o [ Console psql ] representado por [ postgres=# ]

    ----------------------------------------------- COMANDOS RELEVANTES -----------------------------------------------
    PostgreSQL Monitor (lista de comandos) [ help ]
    PostgreSQL Monitor (fazer logout)      [ \q ]
    """
