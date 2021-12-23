

"""
Objetivo
     alterar exibição em iteração de vertical para horizontal, com a opção de adição de um espaçador entre os dados
"""

# Dados na vertical (mais padrão)
r = {*range(1, 4)}
for x in r:
    print('*', x)
print('\n')

# Dados na horizontal (menos padrão) usando [ end="" ]
r2 = {*range(1, 4)}
for y in r2:
    print(y, end=' -> ')  # No [ end="" ] adiciona-se um separador, já que os dados vêm na mesma linha
print('\n')
