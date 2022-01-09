

def fonte():
    """
    Curso || Bancos de Dados SQL e NoSQL do básico ao avançado
    Local || Seção 3: Modelagem de Dados
    Aula  || 15. Terceira Forma Normal
    """


def terceira_forma_normal():
    """
    No total, há 5, mas 3 formas normais são mais usadas
    A terceira forma normal é conhecido como 3FN

    --------------------------------------------------- Condição 3FN ---------------------------------------------------
    3FN é dependente da 2FN
    Nenhum chave não primária deve ser dependente de outra numa mesma tabela (chave primária é excluida do contexto),
    havendo exclusão em caso de ser achado uma dependência

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

    ----------------------------------------------------- PROBLEMA -----------------------------------------------------
    O campo [ subtotal ] depende dos campos [ qtd ] e [ v_unit ]

    ---------------------------------------------------- RESOLUÇÃO ----------------------------------------------------
    Exclusão do campo [ subtotal ]




    ----------------------------------------------------- EXEMPLO -----------------------------------------------------
    n_pedido || codigo_produto || qtd || v_unit
    1005     || 1-934          || 5   || 1500
    1006     || 1-956          || 3   || 350
    1007     || 1-923          || 1   || 190
    1008     || 1-908          || 6   || 980

    codigo_produto || produto
    1-934          || impressora laser
    1-956          || impressora desjet
    1-923          || impressora matricial
    1-908          || impressora mobile

    ----------------------------------------------------- PROBLEMA -----------------------------------------------------
    O campo [ v_unit ], deveria estar na segunda tabela, pois aparentemente (eu não consigo entender) este campo
    não parece necessária à chave primária [ n_pedido ]

    ---------------------------------------------------- RESOLUÇÃO ----------------------------------------------------
    Transferir essa chave secundária à segunda tabela, onde parece fazer mais sentido




    ----------------------------------------------------- EXEMPLO -----------------------------------------------------
    n_pedido || codigo_produto || qtd
    1005     || 1-934          || 5
    1006     || 1-956          || 3
    1007     || 1-923          || 1
    1008     || 1-908          || 6

    codigo_produto || produto              || v_unit
    1-934          || impressora laser     || 1500
    1-956          || impressora desjet    || 350
    1-923          || impressora matricial || 190
    1-908          || impressora mobile    || 980
    """