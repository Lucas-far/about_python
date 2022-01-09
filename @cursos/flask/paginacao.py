

def infos():
    """
    ------- CONCEITO -------
    Forma de limitar dados coletados, filtrando a quantidade a ser exibida por vez

    ------- PARÂMETROS PADRÃO -------
    Limit  || Valor limite de objetos exibíveis em uma página
    Offset || Valor limite de saltos

    ------- EXEMPLO -------
    /postagens?limit=10&offset=30

    Máximo de 10 itens mostrados por páginas
    Salto dos 30 primeiros objetos de um banco de dados, exibindo a partir do 31

    ------- DETALHE -------
    Parâmetros são variáveis: /postagens?ano=2018&limit=10&offset=30
    """
