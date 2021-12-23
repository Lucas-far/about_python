

"""
Objetivo
    retornar uma string da documentação (docstring) de uma função (se uma foi criada)
"""

def criar_dicio(chave, valor):
    """ Criar uma classe dicionário """
    return {chave: valor}
print(1, exemplo := criar_dicio.__doc__)

def contar_palavras(texto: str) -> None:
    """ Criar dicionário da quantidade de dados de uma string """
    container = {}                                  # o dicionário
    texto = ''.join(texto)                          # conversão da string de um índice para string com cada índice
    counter = 0                                     # contador do loop
    while counter < len(texto):
        for each_data in texto:
            data = each_data                        # salvar cada letra da string em uma var separado
            data_countage = texto.count(each_data)  # salvar a contagem de letra da string em uma var separada
            container[data] = data_countage         # criando uma chave com duas variáveis criadas anteriormente
            counter += 1
    print(container)
contar_palavras('Lucas Farias')
print(2, contar_palavras.__doc__)
