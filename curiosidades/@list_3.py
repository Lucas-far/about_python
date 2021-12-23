

"""
Curiosidade? Duas formas de retornar o último índice de uma lista
"""

lista = [False, None, True]
print(lista[-1])
print(lista.pop())  # A questão é que ao fazer isso por esse método, você retira o último dado (literal ou var)
print(lista)        # Note que o dado 'True' sumiu
