

"""
Objetivo
    converter classes numéricas de valor negativo para sua versão positiva
"""
# @bool @complex @float @int

def scan(classe, dado):
    try:
        print(classe, dado, abs(dado))
    except TypeError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))

scan('booleano', True)
scan('complexo', -7j)
scan('dicionário', {-7: -7})
scan('flutuante', -7.0)
scan('inteiro', -7)
scan('lista', [-7])
scan('nenhum', None)
scan('range', range(-7, -6))
scan('conjunto', {-7})
scan('string', '-7')
scan('tupla', (-7,))
