

"""
Objetivo:
    palavra reservada usada com o método sorted() para organizar dados dentro de um iterável

Observação:
    1. método interage com outros iteráveis, convertendo-os para classe lista
    2. método também usa outros métodos: min() e max() (necessário pesquisar)
    3. método possui um segundo parâmetro, que inverte a ordem
"""

# Usando sorted() sem o segundo parâmetro
students = [('John', 'catholic', 15), ('Jane', 'jewish', 12), ('Dave', 'muslim', 10)]
print([1], sorted(students))
print([2], sorted(students, key=lambda v: v[0]))  # organizar pelo índice 0
print([3], sorted(students, key=lambda v: v[1]))  # organizar pelo índice 1
print([4], sorted(students, key=lambda v: v[2]))  # organizar pelo índice 2

# Usando sorted() com o segundo parâmetro (inversão)
nome = 'Maurício Freitas'
print([5], sorted(nome, key=lambda v: v == 'i', reverse=True))  # igual segundo [6]
print([5], sorted(nome, key=lambda v: v == 'i'))                # igual primeiro [6]
print([6], sorted(nome, key=lambda v: v != 'i', reverse=True))  # igual segundo [5]
print([6], sorted(nome, key=lambda v: v != 'i'))                # igual primeiro [5]
