

"""
Objetivo:
     filtrar dado(s) em uma classe iterável, retirando ou isolando esse dado

Observação:
    1. funciona sob a influência mandatória da função lambda
    2. na função lambda, trabalha-se majoritariamente com operações relacionais ou condições simples
    3. método dependente de casting ou next() para convertê-lo num objeto visível
"""

# TODO -> também pode ser feito com: range e tupla

# Conjunto
cj = {True, 7j, 7.0, 7, None, 's', ('t',)}
print(1, cjfil := list(filter(lambda x: x == 7j, cj)))    # isolar
print(2, cjfil2 := list(filter(lambda x: x != 7.0, cj)))  # retirar

# Dicionário
d = {True: False, 7j: -7j, 'd': {'c': 'v'}, 7.0: -7.0, 7: -7, None: None, 's': 'S', ('t',): ('T',)}
print(3, dfil := list(filter(lambda x: x == 's', d)))      # isolar
print(4, dfil2 := list(filter(lambda x: x != ('t',), d)))  # retirar

# Lista
l = [True, 7j, {'c': 'v'}, 7.0, 7, ['l'], None, {'cj'}, 's', ('t',)]
print(5, lfil := list(filter(lambda x: x is None, l)))       # isolar
print(6, lfil2 := list(filter(lambda x: x is not True, l)))  # retirar

# String
s = 'Albuquerque'
print(7, sfil := ''.join(list(filter(lambda x: x == 'b', s))))
print(8, sfil2 := ''.join(list(filter(lambda x: x != 'A', s))))
print(9, sfil3 := ''.join(list(filter(lambda x: x != 'q' and x != 'u' and x != 'e', s))))

# filter() + if..........se string 'a' existe em algum dos dados da var abaixo
nome = ['Tereso', 'Marcos', 'Alfredo', 'de', 'Palmeira']
print(10, nomefil := ' '.join(list(filter(lambda x: x if 'a' in x else None, nome))))

# filter() + if + next()
nomefil2 = filter(lambda x: x if 'e' in x else None, nome)
next(nomefil2)         # o primeiro dado é saltado, pela ausência do print()
print(11, next(nomefil2))  # o segundo dado é impresso
