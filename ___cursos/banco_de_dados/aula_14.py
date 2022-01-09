

def fonte():
    """
    Curso || Bancos de Dados SQL e NoSQL do básico ao avançado
    Local || Seção 3:Modelagem de Dados
    Aula  || 14. Segunda Forma Normal
    """


def segunda_forma_normal():
    """
    No total, há 5, mas 3 formas normais são mais usadas
    A segunda forma normal é conhecida como 2FN

    --------------------------------------------------- Condição 2FN ---------------------------------------------------
    2FN é dependente da 1FN, ou seja, para avançar na construção de uma tabela, ela não deve ter campos multivalorados
    As chaves secundárias devem ser atributos da chave primária

    ----------------------------------------------------- EXEMPLO -----------------------------------------------------
    n_pedido || codigo_produto || produto              || qtd || v_unit || subtotal
    1005     || 1-934          || impressora laser     || 5   || 1500   || 7500
    1006     || 1-956          || impressora desjet    || 3   || 350    || 1050
    1007     || 1-923          || impressora matricial || 1   || 190    || 190
    1008     || 1-908          || impressora mobile    || 6   || 980    || 5880

    ----------------------------------------------- FORMA DE INTERPRETAR -----------------------------------------------
    Uma forma de entender a 2FN é olhando para os campos secundário e se perguntar: - Esse campo parece ser um atributo
    legítimo para a chave primária?

    ----------------------------------------------------- PROBLEMA -----------------------------------------------------
    O campo [ produto ] possui a mesma função do campo [ n_pedido ], que é o de identificador
    O campo [ produto ] não é dependente do campo [ n_pedido ], ele é a mesma coisa

    ---------------------------------------------------- RESOLUÇÃO ----------------------------------------------------
    Criar uma segunda tabela onde o campo [ produto ] ache uma relação com outro
    Nesse caso, o campo [ produto ] pode ser atributo do campo [ codigo_produto ]
    Note que a primeira tabela deve ter um campo passado para a segunda tabela, para que haja uma relação




    ----------------------------------------------------- EXEMPLO -----------------------------------------------------
    n_pedido || codigo_produto || qtd || v_unit || subtotal
    1005     || 1-934          || 5   || 1500   || 7500
    1006     || 1-956          || 3   || 350    || 1050
    1007     || 1-923          || 1   || 190    || 190
    1008     || 1-908          || 6   || 980    || 5880

    codigo_produto || produto
    1-934          || impressora laser
    1-956          || impressora desjet
    1-923          || impressora matricial
    1-908          || impressora mobile
    """


def detalhe_da_aula():
    """
    O campo [ v_unit ] do exemplo acima, deveria ser retirado da primeira tabela para a segunda, mas o professor disse
    que essa coreção não será feita devido a questão de melhorar a compreensão da 3FN
    """