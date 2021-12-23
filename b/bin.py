

"""
Objetivo:
    converter classe inteira para sua versão binária

Observação:
    1. os dois primeiros índices do retorno do método, não fazem parte da conversão, então eles são ignorados
"""

# @bool @int

def scan(classe, dado):
    try:
        print(classe, dado, bin(dado)[2:])  # [2:] ignorar os dois primeiros índices
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

i = 70
i = str(bin(i))[2:]  # converte-se para string para poder retirar omitir os dois primeiros índices
print([1], i)

# Exemplo alternativo de mesmo resultado
print([2], i2 := format(70, 'b'))
