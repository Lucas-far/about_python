

# Configuração de um usuário novo através do usuário matriz
def tutorial_padrao_com_problemas():
    """
    • mysql -u root -p
    • Inserir a senha configurado na instalação

    • CREATE USER 'nome do usuário novo'@'localhost' IDENTIFIED BY 'senha desejada';
        Se nada tiver sido feito errado, o retorno deve ser [ Query OK, 0 rows affected ]

    • exit
    • mysql -u usuário novo -p
    • Inserir a senha configurado para este usuário novo

    ---------------------------------------------------- PROBLEMAS ----------------------------------------------------
    • Independente de estar logado no usuário 'root' ou no novo, o comando 'GRANT' parece não funcionar
    • O comando configura para que um usuário novo tenha os mesmo privilégios do usuário matriz

        GRANT ALL PRIVILEGES ON *.* TO 'nome do usuário novo' WITH GRANT OPTION;
        FLUSH PRIVILEGES
    """


def tutorial_oficial():
    """
    ------------------------------------------------------ LOGIN ------------------------------------------------------
    • mysql -u root -p
    • Inserir a senha configurado na instalação

    -------------------------------------------------- CRIAR USUÁRIO --------------------------------------------------
    • CREATE USER 'nome do usuário novo'@'localhost' IDENTIFIED BY 'senha desejada';

    -------------------------------------- TORNAR USUÁRIO ADMIN (SOLUÇÃO PESSOAL) --------------------------------------
    • Antes de mais nada, é preciso que um usuário novo já tenha sido criado pelo usuário matriz
    • Entrar no [ MySQL Workbench local instance ], logar na minha conta 'root'
    • Ao logar, há um painel esquerdo [ MANAGEMENT - Users and Privileges ]
    • No painel, aparecem cada um dos usuários já criados, além do 'root'
    • Clicar no nome do usuário a ser alterado e depois clicar na aba [ administrative roles ]
    • Marcar a primeira caixa (que marcará todas as outras) e clicar em [ apply ]

    ----------------------------------------------- ACESSO PELO TERMINAL -----------------------------------------------
    O usuário, antes comum, após tornar-se ADMIN, deve conseguir fazer acesso normalmente pelo console do MySQL
    Comando: [ mysql -u nome_user -p ] seguido da [ senha ] definida
    """
