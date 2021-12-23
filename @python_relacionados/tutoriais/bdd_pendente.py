""""""

# https://www.youtube.com/watch?v=J5q7s7l2EuI     Notação Posicional - Bases Numéricas #01
# https://www.youtube.com/watch?v=Uh2ebFW8OYM     Python Tutorial: File Objects - Reading and Writing to Files
# https://www.youtube.com/watch?v=ZiC5NgSGJXU     Python Exercício #041 - Classificando Atletas
# https://www.youtube.com/watch?v=yTQDbqmv8Ho     Curso introdutório de Python
# https://www.youtube.com/watch?v=q5uM4VKywbA     Python Tutorial: CSV Module - How to Read, Parse, and Write CSV Files
# https://www.youtube.com/watch?v=bi1dB284tpo     Coisas que precisa saber para fazer seu jogo: Funções - Jogo em Python
# https://www.youtube.com/watch?v=NR1RKt6NT8s     Exercício Python #046 - Contagem regressiva
# https://realpython.com/documenting-python-code/#docstrings-background
# https://edabit.com/challenge/vudQZFD64nDWkKz8a
# https://www.youtube.com/watch?v=36BE91DxoHE     Criação de ambiente virtual e instalação django
# https://www.youtube.com/watch?v=F5mRW0jo-U4     14:00
# Aula 164 [ 12:00 ]



# Algoritmo para brincar
# "======================================================================================================================"
# from time import sleep
# nome = 'Eu me chamo Lucas'
# lista = []
# contar = 0
#
# while True:
#     for each_data in nome:
#         lista.append(each_data)
#         print(str(contar), lista)
#         sleep(0.25)
#         contar += 1
#     if len(lista) == len(lista):
#         contar = 0
#         while len(lista) > 0:
#             lista.pop()
#             print(str(contar), lista)
#             contar += 1
#             sleep(0.25)
#     contar = 0
# "======================================================================================================================"



# Complemento de tratamento de erro para dados aceitáveis, mas com disposição estranha
"======================================================================================================================"
# var = 'L U C A Sfarias'
# while True:
#     index = var.index(' ')
#     var = var.replace(var[index], '')
#     var = var.lower()
#     var = var.upper()
#     var = ' '.join(var)
#     break
# print(var)
"======================================================================================================================"



# Trocando texto por traços e deixando os espaços
"======================================================================================================================"
# input_sentence = input('Digite um texto -> ')
# container = input_sentence
# input_sentence = list(input_sentence)
# index = 0
# checker = []
# punctuation_dash = []
# while index < len(input_sentence):
#     checker.append(input_sentence[index] != ' ')
#     index += 1
#
# for each_data in checker:
#     if each_data is True:
#         punctuation_dash.append('_')
#     else:
#         punctuation_dash.append(' ')
# index = 0
# del checker
#
# punctuation_dash = ''.join(punctuation_dash)
# print(container)
# print(punctuation_dash)
"======================================================================================================================"



# Exibidor de caracteres de frases gradativos
"======================================================================================================================"
# from time import sleep
# data = input('Provide a sentence, please -> ')
# counter = 0
# initial_index = 0
# ending_index = 1
# var = data.split()
# biggest_data = sorted([len(each_data) for each_data in var]).pop()
#
# while counter < biggest_data:
#     print(' '.join(list(each_data[initial_index:ending_index] for each_data in var)))
#     sleep(1)
#     ending_index += 1
#     counter += 1
"======================================================================================================================"



# Função de contagem regressiva
"======================================================================================================================"
# from time import sleep
#
#
# def countdown_and_speed(amount: int = 0, speed: float = 1):
#     while amount > 0:
#         if not amount % 25:
#             print('\n')
#             print(amount, end=' ')
#             sleep(speed)
#             amount -= 1
#         else:
#             print(amount, end=' ')
#             sleep(speed)
#             amount -= 1
#
# countdown_and_speed(-70, 0.2)
"======================================================================================================================"
