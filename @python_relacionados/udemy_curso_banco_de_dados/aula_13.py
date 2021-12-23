

def fonte():
    """
    Curso || Bancos de Dados SQL e NoSQL do básico ao avançado
    Local || Seção 3:Modelagem de Dados
    Aula  || 13. Primeira Forma Normal
    """


def primeira_forma_normal():
    """
    No total, há 5, mas 3 formas normais são mais usadas
    A primeira forma normal é conhecida como 1FN
    1FN é uma aplicadora de regras de normalização em tabelas

    --------------------------------------------------- Condição 1FN ---------------------------------------------------
    Todos os seus campos possuirem valor singular

    ----------------------------------------------------- DETALHE -----------------------------------------------------
    Tabelas não devem possuir campos nulos, caso contrário, é uma tabela problemática
    """


def exemplo():
    """
    ----------------------------------------------------- EXEMPLO -----------------------------------------------------
    Código cliente || Nome  || Telefone                   || Endereço
    C001           || José  || ('9563-6352', '9847-2501') || ('Rua Seis 85', 'Morumbi', '12536-965')
    C002           || Maria || 3265-8596                  || ('Rua Onze 64', 'Moema', '65985-963')
    C003           || Janio || ('8545-8956', '9598-6301') || ('Praça Ramos', 'Liberdade', '68858-633')

    ----------------------------------------------------- PROBLEMA -----------------------------------------------------
    O campo [ endereço ] é multivalorado

    ---------------------------------------------------- RESOLUÇÃO ----------------------------------------------------
    Substituição do campo [ endereço ] por campos novos que representem esse campo, mas sem criar campos multivalorados





    ----------------------------------------------------- EXEMPLO -----------------------------------------------------
    Código cliente || Nome  || Telefone                   || Rua         || Bairro    || CEP
    C001           || José  || ('9563-6352', '9847-2501') || Rua Seis 85 || Morumbi   || 12536-965
    C002           || Maria || 3265-8596                  || Rua Onze 64 || Moema     || 65985-963
    C003           || Janio || ('8545-8956', '9598-6301') || Praça Ramos || Liberdade || 68858-633

    ----------------------------------------------------- PROBLEMA -----------------------------------------------------
    Apesar de corrigir a maioria dos campos, inserindo novos, um dos campos ainda permaneçe multivalorado: [ telefone ]

    ---------------------------------------------------- RESOLUÇÃO ----------------------------------------------------
    Criar um segunda tabela que trate dados multivaloradis, notando que as duas tabelas se relacionam por um campo. Para
    não quebrar a regra da 1FN, um ID passará a ter mais de um valor, mas sem criar campos multivalorados





    ----------------------------------------------------- EXEMPLO -----------------------------------------------------
    Código cliente || Nome  || Rua         || Bairro    || CEP
    C001           || José  || Rua Seis 85 || Morumbi   || 12536-965
    C002           || Maria || Rua Onze 64 || Moema     || 65985-963
    C003           || Janio || Praça Ramos || Liberdade || 68858-633

    Código cliente || Telefone
    C001           || 9563-6352
    C001           || 9847-2501
    C002           || 3265-8596
    C003           || 8545-8956
    C003           || 9598-6301
    """