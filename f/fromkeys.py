

"""
Objetivo:
     criação alternativa (incomum) de dicionário

Observação:
    1. se a chave for uma string, cada letra torna-se uma nova chave
    2. se a chave for uma conjunto/lista/range/tupla, cada índice torna-se uma nova chave
"""

def scan(classe, chave, valor):
    try:
        print(classe, {}.fromkeys(chave, valor))
    except TypeError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))

scan('booleano', True, False)  # Em um dicionario padrão, isso funciona, mas aqui, não
scan('complexo', 1j, -1j)
scan('dicionário', {'c': 'v'}, {'ch': 'vl'})
scan('flutuante', 2.0, -2.0)
scan('inteiro', 3, -3)
scan('lista', ['l'], ['ist'])
scan('nenhum', None, None)
scan('range', range(1, 4), 0)
scan('conjunto', {'cj'}, {'jc'})
scan('string', 's', 'S')
scan('tupla', ('t',), 'T')
