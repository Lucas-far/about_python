

"""
Objetivo:
    Filtrar através de um inteiro, o número de ocorrência de letras, caso classe string
    Filtrar através de um inteiro, o número de ocorrência de palavras, caso outras classes iteráveis

Observação:
    método dependente de outro: Counter()
    método gerador de lista com dados tupla, ao invés de dicionário
    método não faz sentido ser usado com classes: conjunto, dicionário
    em conjunto, dados não repetem-se
    em dicionário, chaves não repetem-se
"""

from collections import Counter

# @list @range @set @str @tuple

def scan(classe, dado):
    try:
        print(classe, Counter(dado).most_common(3))
    except TypeError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))

scan('booleano', True)
scan('complexo', 7j)
scan('dicionário', {1: None, 2: None, 3: None})
scan('flutuante', 7.0)
scan('inteiro', 7)
scan('lista', [1, 4, 5, 1, 5, 5, 4])
scan('nenhum', None)
scan('range', range(1, 4))
scan('conjunto', {'a', 1, 'b', 2})
scan('string', 'classe string')
scan('tupla', ('c', 'l', 'a', 's', 's', 'e', 't', 'u', 'p', 'l', 'a'))

print([1], Counter('t2vsd4m3fov5w4vul4faks2wxydc3uxomfomh25qoehvlvbqig4no6tasznizlgxewx7os').most_common(2))
print([2], l :=
      Counter("""
      Olá, Lucas Farias Santos,
      Sua senha de login foi alterada. Se você acha que isso seja um erro, clique no botão abaixo para acessar
      nosso portal de suporte, onde você poderá entrar em contato com nossa equipe de suporte. Entre em contato
      com a equipe de suporte
      """.split()).most_common(3))
