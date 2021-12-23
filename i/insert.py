

"""
Objetivo:
     inserir um dado dentro de uma classe iterável lista

Observação:
    1. o método possui 2 parâmetros mandatórios
    2. por ser uma lista, qualquer dado de classe pode ser adicionado, não apenas dados iteráveis
    3. Lógica: var.insert(ínt=índice onde o dado será inserido ,dado)
    4. Se o índice fornecido não existir, mas for positivo, o dado é inserido no último índice
"""

# @list

def scan(classe, dado, index, dado2):
    try:
        var = dado
        var.insert(index, dado2)
        print(classe, var)
    except AttributeError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))

scan('booleano', True, 0, False)
scan('complexo', 7j, 0, 3j)
scan('dicionário', {'c': 'v'}, 0, {'c2': 'h2'})
scan('flutuante', 7.0, 0, 3)
scan('inteiro', 7, 0, 3)
scan('lista', ['l'], 1, 'L')
scan('nenhum', None, 0, 'N')
scan('range', range(1, 4), 0, range(5))
scan('conjunto', {'cj'}, 0, 'CJ')
scan('string', 's', 0, 'S')
scan('tupla', ('t',), 0, 'T')
