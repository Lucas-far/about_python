

"""
Curiosidade? construtores [ max() ] e [ min() ] só funcionam se seus dados forem todos os mesmos
"""

lista_int = [1, 2]
lista_str = ['1', '2']
lista_vogais = [*'a.e.i.o.U'.split('.')]
lista_vogais2 = [*'a.e.i.o.u'.split('.')]
lista_vogais_inteiros = [*'a.e.i.o.u.1.2.3'.split('.')]
lista_hibrida = [*lista_int, *lista_str]

# print(max(lista_hibrida))  # TypeError: '>' not supported between instances of 'str' and 'int'
# print(min(lista_hibrida))  # TypeError: '>' not supported between instances of 'str' and 'int'

print(f'[1] Da lista {lista_int}, o maior dado é: {max(lista_int)}')
print(f'[2] Da lista {lista_int}, o menor dado é: {min(lista_int)}')

print(f'[3] Da lista {lista_str}, o maior dado é: {max(lista_str)}')
print(f'[4] Da lista {lista_str}, o menor dado é: {min(lista_str)}')

# Quando todos os caracteres não são de cacha similar, o construtor [ min ] coloca cacha alta por último
print(f'[5] Da lista {lista_vogais}, o maior dado é: {max(lista_vogais)}')
print(f'[6] Da lista {lista_vogais}, o menor dado é: {min(lista_vogais)}')

# Quando todos os caracteres são cacha baixa, a ordem segue a lógica natural
print(f'[7] Da lista {lista_vogais2}, o maior dado é: {max(lista_vogais2)}')
print(f'[8] Da lista {lista_vogais2}, o menor dado é: {min(lista_vogais2)}')

# Quando os caracteres são misturados em tipos, a precedência segue letras e números
print(f'[9] Da lista {lista_vogais_inteiros}, o maior dado é: {max(lista_vogais_inteiros)}')
print(f'[10] Da lista {lista_vogais_inteiros}, o menor dado é: {min(lista_vogais_inteiros)}')
