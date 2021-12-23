

"""
Objetivo:
    retornar o número inteiro do índice de um caractere procurado, da esquerda para a direita

Observação:
    1. se o dado procurado repetir-se, o método retorna o primeiro encontrado
    2. esse método é igual ao método [ index() ], porém menos completo
    3. o método é programado para contar de forma indexada, ou seja, a contagem começa do zero
    4. para uma contagem exata, recomenda-se somar com + 1 após o uso do método
"""

# @list @range @str @tuple

def scan(classe, dado, valor):
    try:
        print(classe, dado.count(valor))
    except AttributeError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))

scan('booleano', True, True)
scan('complexo', 7j, 3j)
scan('dicionário', {'c': 'v'}, 'c')
scan('flutuante', 7.0, 7.0)
scan('inteiro', 7, 7)
scan('lista', ['l'], 'l')
scan('nenhum', None, None)
scan('range', range(1, 4), 2)
scan('conjunto', {'cj'}, 'cj')
scan('string', 's', 's')
scan('tupla', ('t',), ('t',))

# # Qual a diferença entre os métodos [ find() ] e [ index() ]?
"O método [ index() ] é mais completo, pois é possível filtrar a procura, especificando os índices: inicial e final"

# TODO -> 172737 (se o dado procurado for até o último índice, especifica-se ele somando + 1) (exemplo no item 3)
" TODO -> 012345"

print(1, i := '172737'.find('7'))
print(2, i2 := '172737'.index('7', 2))     # o parâmetro 2 significa o índice exato, não acontecendo no parâmetro 3
print(3, i3 := '172737'.index('7', 4, 6))  # 6 > len(i3), mas é usado quando a procura for até o final
