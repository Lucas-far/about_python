

# Criação de um usuário 'não root' pelo interface (Pgadmin)
def parte_1():
    """
    ----------------------------------------------------- DETALHES -----------------------------------------------------
    • Abrir o software [ Pgadmin4 ] (aplicação web)
    • Na abertura, sempre é requisitado a senha do usuário do seu SO
    • Na lateral esquerda há um painel com um dropdown [ Servers ] que dá acesso a dropdowns aninhados
    • É apartir do dropdown [ Servers ] que se começa

    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    • Servers (clicar)
      PostgreSQL13 (servidor padrão) (clicar)
      Login/Group Roles (botão direto) -> create -> login/group role

    --------------------------------------------------- CONFIGURAÇÃO ---------------------------------------------------
    • General     || Name     = nome do usuário 'não root'
    • Definition  || Password = senha do usuário 'não root'
    • Privileges  || Modificar para [ Yes ] as opções [ Can login? ] e [ Superuser? ]
    • [ Save ]
    """


# Não tenho certeza se funciona ainda
def outra_forma():
    """
    1 - sudo su - postgres
    2 - psql
    3 - CREATE USER nome do usuário novo WITH PASSWORD 'senha desejada';
    4 - ALTER USER nome do usuário novo WITH SUPERUSER;
    5 - \q
    6 - exit

    DELETANDO USUÁRIO ROOT OU OUTROS
    7 - sudo su - postgres
    8 - dropuser nome_do_usuário
    """
