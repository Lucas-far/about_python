

"""
Objetivo:
     retornar o número inteiro do índice de um caractere procurado, da esquerda para a direita

Observação:
    1. O método possui de 1 até 3 parâmetros, sendo apenas o primeiro, mandatório
    2. Os parâmetros: var.index('dado procurado', int=índice inicial, int=índice final)
    3. Se o dado não existir no iterável alvo, o método gera [ ValueError ]
"""

# @list @range @string @tuple

def scan(classe, dado, indice):
    try:
        print(classe, dado.index(indice))
    except AttributeError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))
    except ValueError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))

scan('booleano', True, True)
scan('complexo', 7j, 2j)
scan('dicionário', {'c': 'v'}, 'c')
scan('flutuante', 7.0, 3.0)
scan('inteiro', 7, 5)
scan('lista', ['l'], 'l')
scan('nenhum', None, 'o')
scan('range', range(1, 4), 3)
scan('conjunto', {'cj'}, 'cj')
scan('string', 's', 's')
scan('tupla', ('t',), 't')

# Pode-se procurar o índice de um dado dentro de um iterável, ao invés de uma pesquisa global no iterável
print(['lista', 'item 2'][0].index('t'))

# Usando os parâmetros
print([2], range(1, 11).index(7))                       # 1 parâmetro
print([3], 'Habilidade'.index('l', 2))                  # 2 parâmetros
print([4], ('a', 'b', 'c', 'd', 'e').index('d', 1, 4))  # 3 parâmetros
