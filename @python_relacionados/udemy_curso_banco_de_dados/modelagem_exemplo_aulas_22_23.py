

def fontes():
    """
    Seção 3: Modelagem de Dados - 22. Exercício Modelagem de Dados
    Seção 3: Modelagem de Dados - 23. Correção Exercício Modelagem de Dados
    """


# Coletagem de dados através da interpretação do enunciado
def aula_22():
    """
    Empresa: Fabricante de picolé

    Picolés (dados)                  1. água              | 2. ao leite        |                    |
    Picolés (água) (dados)           1. sabor             | 2. ingredientes    | 3. preço           | 4. tipo embalagem
    Picolés (leite) (dados)          1. sabor             | 2. ingredientes    | 3. preço           | 4. tipo embalagem
    Pícolé (água) (aditivos)         1. vitaminas         | 2. sais minerais   |                    |
    Pícolé (água) (aditivos) (dados) 1. nome              | 2. fórmula química |                    |
    Pícolé (leite)                   1. conservantes      |                    |                    |
    Pícolé (leite) (conservantes)    1. nome              | 2. descrição       |                    |
    Pícole (água) (lote)             1. normal            |                    |                    |
    Pícole (leite) (lote)            1. ao leite          |                    |                    |
    Revendedores (dados)             1. pessoa de contato | 2. CNPJ            | 3. razão Social    |
    Nota fiscal (dados)              1. data              | 2. validade        | 3. número de série | 4. descrição
    """


def criar_modelo_mysql_workbench():
    """
    - Abertura do MySQL Workbench
    - Menu lateral [ item do meio = criar modelos ]
    - Botão de +
    - Duplo clique no item abaixo do texto [ Physical Schemas ]
    - Inserir um nome ao campo [ Name ]
    - Clicar no ícone do [ disquete ]
    - Inserir o nome novamente e [ Salvar ]
    - Fechar a janela que foi aberta
    - Duplo clique em [ Add diagram + ]

    --------------------------------------------------- CRIAR TABELA ---------------------------------------------------
    Na aba [ Diagram ] temos um conjunto de dropdowns
    Escolher o dropdown [ place a new table = T ] e depois clique na tela do diagrama, para que a tabela apareça
    Para cada nova tabela, o procedimento deve ser repetido

    ------------------------------------------------ CONFIGURAR TABELA ------------------------------------------------
    Com a tabela inserida na diagrama, um clique duplo na sua aba abrirá as configurações

    CAMPOS COMUNS A SEREM PREENCHIDOS:
    1. Table name    2. Column name    3. Datatype    4. Caixas de marcar    5. Foreign Keys

    ITEM 4 (LEGENDAS COMUNS)
    1. PK = chave primária    2. NN = campo não nulo    3. AI = auto incremento

    ITEM 5 (DETALHES)
    O item 5 é usado para criar relacionamentos entre tabelas (uma chave primária é usada como referência em outra)
    As opções nesse item são: [ Foreign key name ] [ Referenced table ] [ Column ] [ Referenced columns ]
    No Ubuntu, há uma criação de sintaxe automática o item [ Foreign keys name ]
    Essa sintaxe costuma ser [ fk_nome_da_tabela_int ]

    A aba [ Foreign key name ]  parte da tabela que pega algo emprestado, levando o seu nome
    A aba [ Referenced table ]  é a tabela dona de algum atributo que será herdado
    A aba [ Column ]            atributo herdeiro
    A aba [ Referenced column ] atributo provedor
    """


def aula_23():
    """
    -------------------------------- PROCEDIMENTOS PARA A CRIAÇÃO DE UM BANCO DE DADOS --------------------------------
    1. Encontrar as entidades
    2. Definir os atributos
    3. Definir os relacionamentos
    4. Atentar as formas normais

    --------------------------- ORGANIZAÇÃO DAS ENTIDADES, SEUS ATRIBUTOS E RELACIONAMENTOS ---------------------------
    Entidades
    Picolés             || id, id sabor, preço, id tipo da embalagem
    Tipos de picolé     || id, nome
    Tipo de embalagem   || id, nome
    Ingredientes        || id, nome
    Sabor               || id, nome
    Ingredientes picolé || id, id ingrediente, id picolé
    Aditivos            || id, nome, fórmula química
    Conservantes        || id, nome, descrição
    Aditivos picolé     || id, id aditivo, id picolé
    Conservantes picolé || id, id conservante, id picolé
    Lotes               || id, id tipo picolé, quantidade
    Nota fiscal         || id, data, valor, número de série, descrição, id revendedor
    Lotes nota fiscal   || id, id lote, id nota fiscal
    Revendedor          || id, contato, cnpj, razão social
    """


def aula_23_procedimentos():
    """
    ----------------------------------------------------- DETALHES -----------------------------------------------------
    TABELAS MATRIZ (PROVEDORAS DE CHAVES ESTRANGEIRAS)
    [ aditivos_nutritivos ] (7)
    [ sabores ]             (2)
    [ conservantes ]        (9)
    [ revendedores ]        (14)
    [ tipos picole ]        (4)
    [ tipos_embalagem ]     (3)
    [ ingredientes ]        (5)

    TABELA                           NOME DO CAMPO          TIPO      CARACTERÍSTICAS
    1.1 picoles                    | id                   | INT     | PK NN AI
    2.1 sabores                    | id                   | INT     | PK NN AI
    2.2 sabores                    | nome                 | VARCHAR | NN
    3.1 tipos_embalagem            | id                   | INT     | PK NN AI
    3.2 tipos_embalagem            | nome                 | VARCHAR | NN
    1.2 picoles                    | preco                | DECIMAL | NN
    1.3 picoles                    | id_sabor             | INT     | NN
    1.4 picoles                    | id_tipo_embalagem    | INT     | NN
    4.1 tipos_picole               | id                   | INT     | PK NN AI
    4.2 tipos_picole               | nome                 | VARCHAR | NN
    1.5 picoles                    | id_tipo_picole       | INT     | NN
    5.1 ingredientes               | id                   | INT     | PK NN AI
    5.2 ingredientes               | nome                 | VARCHAR | NN
    6.1 ingredientes_picole        | id                   | INT     | PK NN AI
    6.2 ingredientes_picole        | id_ingrediente       | INT     | NN
    6.3 ingredientes_picole        | id_picole            | INT     | NN
    7.1 aditivos_nutritivos        | id                   | INT     | PK NN AI
    7.2 aditivos_nutritivos        | nome                 | VARCHAR | NN
    7.3 aditivos_nutritivos        | formula_quimica      | VARCHAR | NN
    8.1 aditivos_nutritivos_picole | id                   | INT     | PK NN AI
    8.2 aditivos_nutritivos_picole | id_aditivo_nutritivo | INT     | NN
    8.3 aditivos_nutritivos_picole | id_picole            | INT     | NN
    9.1 conservantes               | id                   | INT     | PK NN AI
    9.2 conservantes               | nome                 | VARCHAR | NN
    9.3 conservantes               | descricao            | VARCHAR | NN
    10.1 conservantes_picole       | id                   | INT     | PK NN AI
    10.2 conservantes_picole       | id_conservante       | INT     | NN
    10.3 conservantes_picole       | id_picole            | INT     | NN
    11.1 lotes                     | id                   | INT     | PK NN AI
    11.1 lotes                     | id_tipo_picole       | INT     | NN
    11.1 lotes                     | quantidade           | INT     | NN
    12.1 notas_fiscais             | id                   | INT     | PK NN AI
    12.1 notas_fiscais             | data                 | DATE    | NN
    12.1 notas_fiscais             | valor                | DECIMAL | NN
    12.1 notas_fiscais             | numero_serie         | VARCHAR | NN
    12.1 notas_fiscais             | descricao            | VARCHAR | NN
    12.1 notas_fiscais             | id_revendedor        | INT     | NN
    13.1 lotes_nota_fiscal         | id                   | INT     | PK NN AI
    13.2 lotes_nota_fiscal         | id_lote              | INT     | NN
    13.3 lotes_nota_fiscal         | id_nota_fiscal       | INT     | NN
    14.1 revendedores              | id                   | INT     | PK NN AI
    14.1 revendedores              | cnpj                 | VARCHAR | NN
    14.1 revendedores              | razao_social         | VARCHAR | NN
    14.1 revendedores              | contato              | VARCHAR | NN

    CHAVES ESTRANGEIRAS
    NOME                               ORIGEM                 BENEFICIÁRIO                                         PROVEDORA
    fk_picoles_1                       sabores                id_sabor (picoles)                                   id (sabores)
    fk_picoles_2                       tipos_embalagem        id_tipo_embalagem (picoles)                          id (tipos_embalagem)
    fk_picoles_3                       tipos_picole           id_tipo_picole (picoles)                             id (tipos_picole)
    fk_ingredientes_picole_1           ingredientes           id_ingrediente (ingredientes_picole)                 id (ingredientes)
    fk_ingredientes_picole_2           picoles                id_picole (ingredientes_picole)                      id (picoles)
    fk_aditivos_nutritivos_picole_1    aditivos_nutritivos    id_aditivo_nutritivo (aditivos_nutritivos_picole)    id (aditivos nutritivos)
    fk_aditivos_nutritivos_picole_2    picoles                id_picole (aditivos_nutritivos_picole)               id (picoles)
    fk_lotes_1                         tipos_picole           id_tipo_picole (lotes)                               id (tipos_picole)
    fk_lotes_nota_fiscal_1             lotes                  id_lotes (lotes_nota_fiscal)                         id (lotes)
    fk_lotes_nota_fiscal_2             notas_fiscais          id_nota_fiscal (lotes_nota_fiscal)                   id (notas fiscais)
    fk_notas_fiscais                   revendedores           id_revendedor (notas_fiscais)                        id (revendedores)
    """
