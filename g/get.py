

"""
Objetivo:
    retornar o valor de uma chave especificada no parâmetro do método

Observação:
    1. se a chave especificada no parâmetro não existir no dicionário, o retorno é None, ou seja, não gera erro
    2. o método possui um parâmetro 2, para inserir uma mensagem string, ativada quando a chave não é encontrada
"""

# @dict

print({'a': 1, 'e': 5, 'i': 9, 'o': 15, 'u': 21}.get('f', 'Dado não encontrado'))  # usando os 2 pars

def scan(classe, dado, chave, msg):
    try:
        print(classe, dado.get(chave, msg))
    except AttributeError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))

scan('booleano', True, 'T', 'ausente')
scan('complexo', 7j, 7j, 'ausente')
scan('dicionário', {'c': 'v'}, 'c', 'ausente')
scan('flutuante', 7.0, 7.0, 'ausente')
scan('inteiro', 7, 7, 'ausente')
scan('lista', ['l'], 'l', 'ausente')
scan('nenhum', None, 'e', 'ausente')
scan('range', range(1, 4), 3, 'ausente')
scan('conjunto', {'cj'}, 'cj', 'ausente')
scan('string', 's', 's', 'ausente')
scan('tupla', ('t',), 't', 'ausente')
