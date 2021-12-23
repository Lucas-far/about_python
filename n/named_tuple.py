

"""
Objetivo:
    chamar uma tupla aparte do método indexado tradicional

Observação:
    1. o segundo parâmetro da variável pode ser uma lista, string ou tupla, mas é mais recomendável uma tupla
"""

from collections import namedtuple

# [ par 1 = rótulo ] [ par 2 = iterável que armazena o nome dos campos ]
l = namedtuple('dados', ['nome', 'email', 'idade', 'país'])  # par2 = lista
s = namedtuple('dados', 'nome, email, idade, país')          # par2 = string
t = namedtuple('dados', ('nome', 'email', 'idade', 'país'))  # par2 = tupla

# Após a criação do [ namedtuple ], cria-se uma segunda var, onde são definidos os argumentos nomeados
dados = l(nome='Lucas', email='l@gmail.com', idade=21, país='Azerbaijão')
dados2 = s(nome='Farias', email='s@outlook.com', idade=40, país='Polônia')
dados3 = t(nome='Santos', email='t@yahoo.com', idade=67, país='Nepal')

# Como as variáveis criadas, são chamadas, na forma padrão? Indexação
print([1], dados[0], dados2[1], dados3[2])

# Como as variáveis criadas, são chamadas, numa forma alternativa? namedtuple()
print([2], dados.nome, dados2.email, dados3.idade)
