

# 33s17iejy3t2a9knmcbi1njgw5gezw69f7gcjp1vnfbpuba3pp4ckunnhc2epgs9fupx2ly1akapweul845y5rbo7cuqv2hzlqhd
# open & with open as
# [ criador e abridor de arquivos para leitura & ou escrita ] [ dependente de métodos .read(), write(), close() ]
# [ criação de arquivo em variável ] [ criação de arquivo em variável integrada ] [ open() dependente de close() ]
# [ with open() independente de close() ]
"======================================================================================================================"
from os import chdir

chdir('c:\\users\\lucas\\desktop')

"Forma não pythônica (variável normal - prefixada)"
arquivo = open('open.txt', 'r')   # abertura de arquivo já existente apenas para leitura
arquivo.close()                   # fechamento mandatório para esse tipo de sintaxe
arquivo2 = open('open.txt', 'w')  # criação de arquivo inexistente para abertura e escrita de dados [ sobreposição ]
arquivo.close()
arquivo3 = open('open.txt', 'a')  # criação de arquivo inexistente para abertura e escrita de dados [ acumulação ]
arquivo.close()

"Forma pythônica (variável incomum - sufixada)"
with open('open.txt', 'r') as file:
    pass
with open('open.txt', 'w') as file2:
    pass
with open('open.txt', 'a') as file3:
    pass

"Se o segundo argumento for r, torna-se inviável a criação/escrita de um arquivo, mas sua leitura é viável"
"Se o segundo argumento for w, torna-se viável a criação de um arquivo, mas sua leitura é inviável"
"Criação/escrita e leitura é melhor recomendável de serem feitas separadamente"

from os import chdir
chdir('c:\\users\\lucas\\desktop')

with open('open.txt', 'w') as doc:
    doc.write('Lucas Farias')

with open('open.txt', 'r') as doc2:
    ler_arquivo = doc2.read()
    print(ler_arquivo)  # Lucas Farias
"======================================================================================================================"



# s3aenvp952u4q9v5n8ge9u3tyhzyy4914wyeczkkjvth2wf6c5oqbnyk6pnz94sc9qc71ja8y6sv6qbmd26yltjyep1j89wcrqrd
# operadores aritméticos
# [ tipo 1 ] [ tipo 2 ] [ tipo 2 apropriado para cálculos em loop for/ while ]
"======================================================================================================================"
contexto_tipo_um = ['print', 'valor da variável', 'variável própria', 'variável nova']
contexto_tipo_dois = ['pós-variável']

inteiro = 1
print(inteiro + -1)  # [ operador aritmético ] [ + ]
inteiro += -1
print(inteiro)       # [ operador aritmético ] [ += ]

inteiro2 = 1 - 1
print(inteiro2)        # [ operador aritmético ] [ - ]
inteiro2 -= 1
print(inteiro2)        # [ operador aritmético ] [ -= ]

inteiro3 = 0
inteiro3 = inteiro3 * inteiro3
print(inteiro3)        # [ operador aritmético ] [ * ]
inteiro3 *= -1
print(inteiro3)        # [ operador aritmético ] [ *= ]

inteiro4 = -1
inteiro5 = inteiro4 / -1
print(inteiro5)        # [ operador aritmético ] [ / ]
inteiro5 /= -1
print(inteiro5)        # [ operador aritmético ] [ / ]

inteiro6 = 1
print(inteiro6 ** -1)  # [ operador arimético ] [ ** ]
inteiro6 **= 0
print(inteiro6)        # [ operador arimético ] [ **= ]

inteiro7 = 2 % 2
print(inteiro7)        # [ operador modular ] [ % ]
inteiro7 %= 1
print(inteiro7)        # [ operador modular ] [ %= ]
"======================================================================================================================"



# wzklb5mfn6atrasvzghcseiq2cd9w8wleg6mzvo6jcmad8l4c2ylu37yhzp3u2z28k8pqpmusqprgcqev1cj1jhins2c9xkltdkt
# operadores condicionais
# [ if = condição inicial ] [ elif = condição alternativa/híbrida  ] [ else = condição adversa ]
# [ if expectativa de condição positiva ] [ não é regra global ]
# [ else expectativa de condição negativa ] [ não é regra global ]
"======================================================================================================================"
from datetime import datetime

dados_de_tempo = datetime.today()
hora = dados_de_tempo.hour
minuto = dados_de_tempo.minute
segundo = dados_de_tempo.second

tempo = '{}h:{}min:{}s'.format(hora, minuto, segundo)
print(tempo)

if hora <= 7:
    print('Hora de acordar')

if minuto >= 30:
    print('Já se passa da metade da hora atual!')
else:
    print('Não chegou a metade da hora atual')

if segundo > 45 <= 59:  # if 45 < segundo <= 59:
    print('O próximo minuto já vai começar')
elif segundo > 30:
    print('Pelo menos 50% do minuto já passou...')
else:
    print('O minuto acabou de começar')
"======================================================================================================================"



# st2p5v3ipptkye1w4cvxods8oxy79cbchn2jrzlgmdaohvarneao6tuk3fgprwe8kgpsmi7gx1af95wfclxxcfwedcgbx3tgrbv9
# operadores lógicos
# [ operador unário     ] [ operador de dúvida       ]
# [ operadores binários ] [ operadores de comparação ]
"======================================================================================================================"
booleano_falso = False
print(booleano_falso is False)              # True [ is ] [ operador unário ] [ operador de dúvida ]

booleano_invertido = not booleano_falso
print(booleano_invertido)                   # True [ not ] [ operador unário ] [ operador de conversão oposta ]

comparar = len('Lucas') < 3                 # False
comparar2 = [1, 2, 3] == [1, 3, 2]          # False
comparar3 = comparar or comparar2           # [ or ] [ operador binário ] [ operador de comparação ]
print(comparar3)                            # False

comparar4 = sum({1, 2, 3, 4, 5}) <= 10      # False
comparar5 = [1, 2, 3] == list(range(1, 4))  # True
comparar6 = comparar4 and comparar5         # [ and ] [ operador binário ] [ operador de comparação ]
print(comparar6)                            # False
"======================================================================================================================"



# 7s9gw3oszyfqrgtcbyryqoimlm4877e19gfl4gt1j3ix58qr3tpdk8zp5uw3x845o4zofx2se8gfu8f99la6rjh9giun1ibp9ll1
# operador modular
# [ sintaxe simples ] vs [ sintaxe refatorada ]
"======================================================================================================================"
var = list(range(1, 28))
var_menor = tuple(range(1, 8))

# Sintaxe simples
var2 = [cada_dado for cada_dado in var if cada_dado % 7 == 0]
print(var2)         # [7, 14, 21]

# Sintaxe refatorada
var4 = [cada_dado for cada_dado in var if not cada_dado % 7]
print(var4)         # [7, 14, 21]

# Sintaxe simples
var3 = (cada_dado for cada_dado in var_menor if cada_dado % 7 != 0)
print(tuple(var3))  # (1, 2, 3, 4, 5, 6)

# Sintaxe refatorada
var5 = (cada_dado for cada_dado in var_menor if cada_dado % 7)
print(tuple(var5))  # (1, 2, 3, 4, 5, 6)
"======================================================================================================================"



# u9gfz8ndercgk6w5j964k3yotbo1txtblxhhhqyx3ewipnf7j75scndo4yk73kwvnqf9v2fwsmygqcdxqhe2m86h34iboebjuga8
# operadores relacionais
# [ operadores binários ] [ comparação entre dados ] [ gerador booleano ]
"======================================================================================================================"
inteiro = len('Lucas')
inteiro2 = sum((1, 2, 3, -4, -5))
inteiro3 = round(27.7)
dicio = {'': ''}
conj = {True}
lista = [0]

print(inteiro < inteiro3)    # True
print(inteiro3 <= inteiro2)  # False
print(inteiro3 > lista[0])   # True
print(lista[0] >= inteiro)   # False
print(conj == dicio)         # False
print(dicio != inteiro2)     # True
"======================================================================================================================"



# 4oymylpljgm2buceeqdoxc9q5q4x7kq994k6kynmhtv4nnupk1h1liqutizlr96enrwkkfdf9qdvhtfvwknonxgq27948tpocp5p
# OrderedDict
# [ importação mandatória ] [ sensível à mudança de ordem ] [ gêmeo de dicionário ]
"======================================================================================================================"
from collections import OrderedDict

dicio_ordenado = OrderedDict({'Lucas': 'Farias', 'Santos de': 'Sousa'})  # Esqueleto de um dicionário  ordenado
dicio_ordenado2 = OrderedDict({'Santos de': 'Sousa', 'Lucas': 'Farias'})

print(dicio_ordenado == dicio_ordenado2)  # False [ OrderedDict ] [ dados iguais em ordens diferentes ]

dicio = {'Lucas': 'Farias', 'Santos de': 'Sousa'}
dicio2 = {'Santos de': 'Sousa', 'Lucas': 'Farias'}

print(dicio == dicio2)  # True [ dicionário ] [ dados iguais em ordens diferentes, são entendidos como iguais ]
"======================================================================================================================"



# dhm6qdrdfyd8q7ax43ilbi18do7xahypflhk2p72jva6rtfoor8ks231ik2sgvqdm6r8ra9f7ck93uzk4estrlhvxp33wzlbsl2b
# path
# [ importação mandatória ] [ sub-métodos ] -> [ path.exists ] [ path.isabs ] [ path.join(getcwd(), '') ]
"======================================================================================================================"
contexto = ['print', 'valor da variável']
from os import chdir, getcwd, path


print(path.exists('C:\\Users\\Lucas\\Desktop'))         # True  [ existe?     ] [ retorno True  ]
print(path.exists('C:\\Users\\Lucas\\Desktop\\main_'))  # False [ não existe? ] [ retorno False ]

desktop = path.exists('C:\\Users\\Lucas\\Downloads')
print(desktop)                                          # True

desktop2 = 'C:\\Users\\Lucas\\Downloads'
print(path.isabs(desktop2))                             # True

chdir('C:\\Users\\Lucas\\Desktop')
print(getcwd())                           # C:\Users\Lucas\Desktop [ diretório atual ]

pasta_main = path.join(getcwd(), 'main')  # União do [ diretório atual ] com um diretório chamado [ main ]
                                          # path.join() dispensa a barra de escape [ \\ ]

print(pasta_main)                         # C:\Users\Lucas\Desktop\main
pasta_imagens = path.join(getcwd(), 'type_image', 'image_amusing')
print(pasta_imagens)                      # C:\Users\Lucas\Desktop\type_image\image_amusing
"======================================================================================================================"



# 751h4az8iw467kuhln7mg539rdrov3oka3nos6vsq71olk4m2j5pav12iqouxa51vu359g6wn97dfgj1akuglqjpy8mieie3k6if
# pi
# [ importação mandatória ] [ valor flutuante matemático constante ] [ valor armazenado em var ]
"======================================================================================================================"
contexto = ['print', 'valor da variável', 'variável própria', 'variável nova']
from math import pi

print(pi)               # 3.141592653589793

dado_elevado_pi = 2892458 ** pi
print(dado_elevado_pi)  # 1.9891573243574e+20
"======================================================================================================================"



# g2s3k9xpdt4mjj596pp1ppyvp6mhmsgtt51ku6fq2j14s1t35h5gfw5go7xhilser67hdqruqk65xgiucq9otynh5sfz9qxos61q
# pipe |
# [ exclusivo conjunto ] [ args múltiplos ] [ clone simplificado do método .union() ]
# [ união de dados em conjunto diferentes ]
"======================================================================================================================"
contexto = ['print', 'variável nova']

conj = {1, 2, 7}
conj2 = {5, 6, 7, 8, 9}
conj3 = {3, 4, 5, 7, 2, 3, 7}
conj4 = conj | conj2 | conj3
print(conj4)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
"======================================================================================================================"



# mgke15o954k9bvvtwp3u8fm4yntutxa2rwsipxd77v4qez7p1k4xbekkq8zlus73coy9d57b4su6kvtd39joi4bmwoj6elo5rh6a
# platform
"======================================================================================================================"
from sys import platform

mgke1_contexto = 'print', 'declaração'

obs = 'importação mandatória'

platform_objetivo = 'informar tipo de sistema operacional'

# Uso em print
print('A plataforma usada nesse laptop é: {}'.format(platform))  # A plataforma usada nesse laptop é: win32

# Uso em declaração
var = platform
print('A plataforma usada nesse laptop é:', var)                 # A plataforma usada nesse laptop é: win32
"======================================================================================================================"



# 6gdhglezmqhcso5tfm9n9c96auf23igcc4q3u9bic32i1gq611nnrgdmaaqtrwatektvxue2bp38ktjs9lvftf5ne4pl9dm78imz
# playsound
# [ importação mandatória ] [ abertura de arquivo de som por meio interno ]
"======================================================================================================================"
from playsound import playsound

playsound('theroom.mp3')
"======================================================================================================================"



# dtd3zozdwes1gegekd4uisekt3xbgo1cgv1f7qcw78sq1llpzu84u6s4mdlbvozzbj2m7hady71hdf2llg1gljmm2efpaatzp1wm
# pop
# [ exclusivo lista / dicionário ] [ armazenamento em variável possível ] [ lista exclusor de último dado ]
# [ lista 0 ou 1 arg = último índice, nº do índice do dado ] [ dicionário 1 arg = chave ]
"======================================================================================================================"
"OBS"  # [ pop() ] remove pelo nº do índice ou o último índice [ limitado ]
"OBS"  # Como tornar [ pop() ] mais eficiente? unindo ele ao método [ index() ]
"OBS"  # var.pop(var.index(dado_a_ser_excluído))

contexto = ('valor da variável', 'pós-variável',)

lista = ['Lucas', 'Farias', 'Santos', 'de', 'Sousa']

print(lista)  # ['Lucas', 'Farias', 'Santos', 'de', 'Sousa']
lista.pop()   # [ lista último dado exclusor ]
print(lista)  # ['Lucas', 'Farias', 'Santos', 'de']
lista.pop(3)  # lista específico dado exclusor ]
print(lista)  # ['Lucas', 'Farias', 'Santos']

dicio = {3: 'dia', 4: 'mês', 2020: 'ano'}
print(dicio)  # {3: 'dia', 4: 'mês', 2020: 'ano'}
dicio.pop(2020)
print(dicio)  # {3: 'dia', 4: 'mês'}
"======================================================================================================================"



# cuab2ekvksayygczc751e1zikp4xznpy9a3626srujppj4d4eqgohmkgwqeox6aj2ofqggtmdd7q6irbsw156kua8emh6c3wk378
# popitem
# [ exclusivo dicionário ] [ dicionário exclusor de último dado ]
"======================================================================================================================"
contexto = ['pós-variável']

dicio = {'Lucas': None, 'Farias': None, 'Santos': None, 'de': None, 'Sousa': None}

print(dicio)  # {'Lucas': None, 'Farias': None, 'Santos': None, 'de': None, 'Sousa': None}
dicio.popitem()
print(dicio)  # {'Lucas': None, 'Farias': None, 'Santos': None, 'de': None}
"======================================================================================================================"



# dt8vgzeg4riy9tav3q6z3tdalvqwtomlrrlk5l58j5q5mxbnir9jkivn1nl96pcxmk37h6v7cpnb41e56qdze17cxx8dhdjx5uok
# popleft
# [ exclusivo deque ] importação mandatória ] [ lista primeiro índice atual exclusor ]
"======================================================================================================================"
contexto = ['pós-variável']
from collections import deque

lista_deque = deque([0, 1, 2, 3, 4, 5])

print(lista_deque)  # deque([0, 1, 2, 3, 4, 5])
lista_deque.popleft()
print(lista_deque)  # deque([1, 2, 3, 4, 5])
"======================================================================================================================"



# dy25gyouwa6q2yo9wx7ciwqau2w8eirncrub1b6egw4effm72u25wb9bm17t82gd6o9hhfh3jf6lt1dqrje73ekmdzjv696eymgu
# position
# [ importação mandatória ] [ automação ] [ retornador de coordenadas = x, y da posição na tela]
# [ parâmetro sem argumento ]
"======================================================================================================================"
contexto = ('print', 'valor da variável')
from pyautogui import position

var_coordenada = position()
print(var_coordenada)                               # Point(x=308, y=506)
print('A posição do mouse atual é : ', position())  # A posição do mouse atual é :  Point(x=505, y=542)
"======================================================================================================================"



# z7719rysv3lac6r6uubmgn6ixfvzvgpzucuxlxn1oyk9ljanlvzcma5gy5mwwy1ggk4kz97j2f27ymylioeu3mdv15t6u34afoaf
# raise
# [ palavra reservada ] [ levantamento de erro customizado ] [ erro em linha ] [ independente de contexto print ]
"======================================================================================================================"
raise TypeError('tipo de dado inválido')

nome = input('Qual o seu nome? -> ')
if 'L' in nome[0]:
    raise ValueError('Desculpe, mas a letra "L" é intolerável')

# Qual o seu nome? -> Lucas
# Traceback (most recent call last):
#   File "C:/Users/Lucas/Envs/lucas/## rascunho 4.py", line 5, in <module>
#     raise ValueError('Desculpe, mas a letra "L" é intolerável')
# ValueError: Desculpe, mas a letra "L" é intolerável
"======================================================================================================================"



# 4rdafcdfjziv5jraoeghnzz2gzz8nzqfni9hb88nrtcd1jg3gdhwylcep2ofwfc1k86ahhmdnvdm4s8h2uopb38ie1vkwecb7pa7
# randint
# [ importação mandatória ] [ 2 args = int ] [ gerador de 1 inteiro aleatórios dentro de uma range ]
"======================================================================================================================"
contexto = ['print', 'valor da variável']
from random import randint

conj = {randint(1, 5), randint(1, 6), randint(1, 7)}
print(conj)  # {2, 6, 7}
"======================================================================================================================"



# dfyqqzprsd4czjikfrms9p441822ruoagurpn9xlklvkxrrmfczjt6mpykdgb7gj1e4uua3my971xjz3o89epxv4crg8yhl4t8ec
# random
# [ importação mandatória ] [ caráter aleatório ] [ gerador de flutuante > 0 < 1 ] [ parâmetro vazio ]
"======================================================================================================================"
contexto = ['print', 'valor da variável']
from random import random

lista = [random(), random(), random()]
print(lista)  # [0.4344048693007443, 0.3998078858227, 0.44487441918588644]
"======================================================================================================================"



# 5o1dzk5jg8o6jkpxt7emlyhyupo92erzr6iokl5be68m9nlcleh1kv5ex184kpg7sw8cl591c25fmb9op5rbfopdxz1qaoccrpmc
# range
# [ até 3 args = nº inicial, nº final, salto ] [ classe parcialmente dependente de desempacotamento ]
# [ range combinado com operador modular ]
"======================================================================================================================"
"Observações:"
# 1. Se há apenas 1 argumento, este é entendido como o segundo argumento (1º argumento torna-se 0)
# 2. O segundo  argumento é: [ não inclusivo' (-1) ] EX: range(1, 8) é na verdade = range(1, 7)
# 3. O terceiro argumento é: [ não mandatório ] e [ inclusivo (dependendo do segundo argumento passado) ]
# 3. Por exemplo:
print(range(1, 10, 3))  # 1, 4, 7
"Interpretação:"        # O range chegaria até 10, pois o 2º argumento criou saltos quebrados
print(range(1, 11, 3))  # 1, 4, 7, 10
"Interpretação:"        # O range chega até 10, pois o 2º argumento criou saltos uniformes

lista_range = list(range(1, 270))

# Range combinado com: [ loop for ] e [ operador aritmético modular ]
for dados in lista_range:
    if not dados % 19:         # Sintaxe refotorada (condição divisíveis por 19)
        print(dados, end=' ')  # 19 38 57 76 95 114 133 152 171 190 209 228 247 266

# Range combinado com: [ tuple comprehension (generator) ]
print(tuple((dados for dados in lista_range if not dados % 19)))
                               # (19, 38, 57, 76, 95, 114, 133, 152, 171, 190, 209, 228, 247, 266)
"======================================================================================================================"



# 6ytm1pai1cber81p9zrt69ekfz6f8ykfvegkz1fu7yuyowodn46nwopc8o3tr7bblf8ysdcf883ew77cpm1cykanodyas2i1occy
# read
# [ leitura de arquivo existente ] [ não criador de arquivo ] [ dependente de construtor open() ] [ parâmetro vazio ]
# [ é permitido apenas uma leitura no escopo, caso haja mais, esta precisa ser desativada ]
"======================================================================================================================"
contexto = ('print', 'variável nova')
from os import chdir

chdir('c:\\users\\lucas\\desktop\\')
with open('metodo_read_exemplo.txt', 'r') as doc:  # O arquivo não pode ser criado, ele já deve ser existente
    # LEITURA POR VARIÁVEL
    read_all = doc.read()
    print(read_all)

    # LEITURA POR PRINT
    # print(doc.read())

    #####################################################
    # LEITURA DE CONTEÚDO GLOBAL (alternativa) (loop for)

    # for each_data in doc:
    #     print(each_data, end='')
    #####################################################
"======================================================================================================================"



# n3c2yzl75wmsc71qzzaxuu1h6aneobpy23xu3xxhfts8b5qpeb2pzeec6754zd41t86pvutmhwf9dp81i57djimhupsmu39ss9hx
# reader
# [ leitura de arquivos .csv ] [ CSV = comma separated values = valores separadors por vírgula ]
# [ criador de lista baseado no separador do documento ]
# [ documento com separador específico selecionado que deve ser imutável ] [ loop for como melhorador de acesso ]
"======================================================================================================================"
contexto = ['valor da variável']

from csv import reader
from os import chdir

chdir('c:\\users\\lucas\\desktop')
with open('arq.csv', 'r') as doc:
    leitura = reader(doc)
    # print(leitura)        # <_csv.reader object at 0x012BFCD8>
    # print(next(leitura))  # ['nome', 'Lucas']
    # print(next(leitura))  # ['sobrenome', 'Farias']

    next(leitura)           # em caso de cabeçalho e a intenção de saltà-lo
                            # [ reader ] gera objeto de memória, por isso é possível usar [ next() ] nele
    for each_data in leitura:
        "Chamada de todos os dados em lista"
        print(each_data)
        # ['nome', 'Lucas']
        # ['sobrenome', 'Farias']
        # ['idade', '27']
        # ['nacionalidade', 'brasileiro']
        # ['cor', 'pardo']
        "Chamada de índice específico"
        print(each_data[0])
        # nome
        # sobrenome
        # idade
        # nacionalidade
        # cor
        "Chamada de índice específico"
        print(each_data[1])
        # Lucas
        # Farias
        # 27
        # brasileiro
        # pardo
"======================================================================================================================"



# uhqh3rti8to3ug6o48c4gpgbgamrln4wccn68m1b6w3w4y6m4n9k5qtcvsgi9xta93jsm6rgxvd5vh7vop7gn1el61fdcqvu8981
# readline
# [ leitura de linha de arquivo ] [ não é criador de arquivo ] [ construtor open() dependente ] [ parâmetro vazio ]
# [ texto em 1ª linha recomendável ] [ duplicação de comando para leitura da próxima linha ]
# [ end='' recomendável para evitar quebra de linha em leitura ] [ leitura de linha invisível/salto de leitura ]
# [ leitura reduzida de linha ]
"======================================================================================================================"
contexto = ('print',)
from os import chdir

chdir('c:\\users\\lucas\\desktop')
with open('open.txt', 'r') as doc:  # A leitura de arquivo funciona somente se já há um arquivo existente
    print(doc.readline(), end='')   # end='' impede o salto de linha
    print(doc.readline(6), end='')  # leitura reduzida de linha ()

"Forma alternativa de leitura sem método [readline()]"
with open('open.txt', 'r') as doc2:
    leitura = doc2.read().split('\n')  # Cada quebra de linha torna-se um dado de lista que serão lidas separadamente
    print(leitura)                     # ['Eu sou Lucas', 'Eu sou Farias', 'Eu sou Santos', 'Eu sou a Universal']
    print(leitura[0])                  # Eu sou Lucas
    print(leitura[1])                  # Eu sou Farias
    print(leitura[2])                  # Eu sou Santos
    print(leitura[3])                  # Eu sou a Universal

    "Leitura parcial de linha específica"  # leitura restrita por indexação aninhada
    print(leitura[1][0:6])                 # Eu sou
"======================================================================================================================"



# tozzcv6b1i1pzd6pn89qk5uwmtzsb57ubvs75s6ha49a7p82zhd92x5fv8ufsvogrj4umz414r3zlmywi5ypf6x9go2e6x84m7jy
# reduce
# [ importação mandatória ] [ dependente de lambda com 2 parâmetros ] [ 2 args = lambda de 2 par, iterador ]
# [ iterador de dados = loof for piorado ]
"======================================================================================================================"
contexto = ['print', 'valor da variável', 'variável própria', 'variável nova']

var = reduce(lambda x, y: x + '\n' + y, {'nome', 'sobrenome', 'idade', 'nacionalidade', 'língua', 'cor de pele'})
print(var)
# cor de pele
# idade
# nacionalidade
# língua
# nome
# sobrenome

var2 = reduce(lambda x, y: x.upper() + '\n' + y.upper(), {'nome', 'sobrenome', 'idade', 'nacionalidade'})
print(var2)

# SOBRENOME
# NOME
# IDADE
# NACIONALIDADE
"======================================================================================================================"



# 4pkk3sszj73s1kkyh8rpgzhl5jdco9ccmqkc3rgg858iqdaleq6kwrvxtdwixqfa4ltxlfbeve25bkcr7wgodse9q1w83hhv3wik
# remove [ método conjunto ]
# [ exclusivo conjunto ] [ 1 arg = dado ] [ exclusão de dado por nome do índice ] [ sensível à KeyError ]
# [ gêmeo do método .discard() ] [ menos eficiente & pythônico que .discard() ]
"======================================================================================================================"
contexto = ('pós-variável',)

"OBS:"  # É possível criar uma variável para excluir um dado de conjunto, mas a IDE considera como uma ação imprópria
conj = {0, 'string'}
# var = conj.remove('string')  # Function 'remove' doesn't return anything
print(conj)                    # {0}

conj = {0, 'string'}
print(conj)  # {0, 'string'}
conj.remove(0)
print(conj)  # {'string'}
"======================================================================================================================"



# r1vf8l2dhg4fby1qcvgvr3lgu44mw5bja3ft7unahkxp717bwlm29cyoyh9wkygw24pmbr9u2aumcsuexgbsxdaj6qu5wukmp8ql
# remove
# [ importação mandatória ] [ método removedor de arquivos (não remove pastas) ]
# [ 1 arg = caminho string até o local do arquivo incluido ] [ excluidor de arquivo definitivo (ctrl + alt + del) ]
"======================================================================================================================"
from os import remove

remove('C:\\Users\\Lucas\\Desktop\\arquivo_renomeado.txt')
"======================================================================================================================"



# 2hx5l423ouzouj7ic7smt7xasm24m1ta5qpc5imauqrdle32eqjulb2bd2sgbrhx34ql42moklzvo9tqcjm2z4s8bt4haxzn5ff6
# rename
# [ importação mandatória ] [ 2 args = dir da pasta/arquivo inclusivo, nome novo ] [ gerenciamento de arquivo ]
# [ renomeador de pasta ou arquivo ] [ conversor ] [ informação de diretório completo mandatório ]
"======================================================================================================================"
from os import rename

rename('C:\\Users\\Lucas\\Desktop\\pasta', 'C:\\Users\\Lucas\\Desktop\\pasta_renomeada')
rename('C:\\Users\\Lucas\\Desktop\\arquivo.txt', 'C:\\Users\\Lucas\\Desktop\\arquivo_renomeado.txt')
rename('C:\\Users\\Lucas\\Desktop\\arquivo.txt', 'C:\\Users\\Lucas\\Desktop\\arquivo_renomeado.pdf')  # conversão
"======================================================================================================================"



# 3e1tbl4mb9pj2mjrm3xl86u7enwqy634z437zy6dzfspf1qbjft5pdsd5shvrmfb1palfbmis3cqdfuv19yrxijlmpee66lhj81q
# replace
# [ exclusivo string ] [ 2 args = dado editável, dado editado ]
# [ redutor/substituidor/implementador de dados em iteráveis ] [ sensível à substituição por classe diferente ]
"======================================================================================================================"
contexto = ['print', 'valor da variável', 'variável própria', 'variável nova']

pais = 'Brasil'
print(pais.replace('Brasil', 'Br'))  # Br

email = 'user@algumacoisa.coisanenhuma'.replace('a', '{}')
print(email)                         # user@{}lgum{}cois{}.cois{}nenhum{}

idade = 27
idade = str(idade).replace(str(idade), '7 anos')
print(idade)                         # 7 anos

email = [email.replace('u', 'lambda')]
print(email)                         # ['lambdaser@{}lglambdam{}cois{}.cois{}nenhlambdam{}']

classe_diferente = 'string'.replace('str', 7)
print(classe_diferente)              #  TypeError: replace() argument 2 must be str, not int
"======================================================================================================================"



# nxmryeu3ixrslj4arzzunu7vavl98fidq8b57yjrisp9l6nq2z2luko2ankzwm5ifad3taqq64imfptjhwwsg5jfujfnj7hqha3h
# replace
# [ importação mandatória ] [ mínimo 3 args = year month day] [ alterador de dados de data & hora atuais ]
# [ alterador de dados de data ] [ uso de argumentos nomeados recomendável (não mandatório) ]
# [ argumentos nomeados = year month day hour minute second microsecond ] [ recomendável seguir a ordem de argumentos ]
"======================================================================================================================"
contexto = ('print', 'variável nova')
from datetime import datetime

"Método [ replace() ] pode ser útil para, por exemplo, mandar e-mails agendados [ não sei como fazer isso ]"

###############################
"Consulta de data e hora atual"
var = datetime.now()
print(var)   # 2020-05-12 10:33:57.355873
###############################

##############################################
"Método [ replace() ] usado de forma indireta"
var2 = var.replace(year=1992, month=12, day=12, hour=19, minute=55, second=11, microsecond=1267)
print(var2)  # 1992-12-12 19:55:11.001267
##############################################

############################################
"Método [ replace() ] usado de forma direta"
viagem_no_tempo = datetime.now().replace(year=1992, month=7, day=16)  # datetime + 2 métodos aninhados
print(viagem_no_tempo)
############################################
"======================================================================================================================"



# ne6t1rocpijv4opwhjigwiktvyk7al5njvr3ria8bb1td9bxh6vlqyc9s7bbg64nyo6xqxp7y8kcf4t5zx97cpewyb8o3lc6qwqo
# repr
# [ importação mandatória ] [ exibição alternativa de datas e hora ] [ dependente do método datetime.now() ]
# [ opinião: não vejo utilidade ]
"======================================================================================================================"
contexto = ('print', 'valor da variável', 'variável própria', 'variável nova')
from datetime import datetime

dados_data_hora = datetime.now()
print(dados_data_hora)        # 2020-05-13 11:28:35.683796
print(repr(dados_data_hora))  # datetime.datetime(2020, 5, 12, 10, 23, 0, 591898)
"======================================================================================================================"



# pzjsp3ioshnddzbbk5ww1ruyjydzv273duqk18yu9ng6s78acsyc3pasiv1gwgy6ku62g7r4wy9kt7o6lbyggqmdtuhezyb5vulb
# reverse
# [ exclusivo lista ] [ vizualização de dados invertida da direita para esquerda ] [ parâmetro vazio ]
"======================================================================================================================"
contexto = ('pós-variável',)

lista = ['a', 'e', 'u', 'a', 'e', 'o', 'i', 'a', 'i']
lista.reverse()
print(lista)  # ['i', 'a', 'i', 'o', 'e', 'a', 'u', 'e', 'a']
"======================================================================================================================"



# iq5elyf132chbsh8bmp6pa2e7kabfi53mi93zwta1wuqlze3kfkw64vyva9id4hjyqgkdrmbenj175bi4g1rroqopqui1uvyhu4q
# reversed
# [ reversor de iteráveis ] [ != de reverse() ] [ 1 arg = dado iterável ] [ objeto de memória ] [ cast mandatório ]
"======================================================================================================================"
contexto = ['print', 'valor da variável', 'variável própria', 'variável nova']

# conj = {True, 0, ''}
# print(reversed(conj))                       # TypeError: 'set' object is not reversible

dicio = {'nome': 'Lucas', 'ano': 2020}
print(tuple(reversed(dicio.items())))         # (('ano', 2020), ('nome', 'Lucas'))

lista = set(reversed([True, 0, '']))
print(lista)                                  # {'', 0, True}

range_ = tuple(range(1, 6))
range2_ = list(reversed(range_))
print(range2_)                                # [5, 4, 3, 2, 1]

string = 'string'
string = tuple(reversed(string))
print(string)                                 # ('g', 'n', 'i', 'r', 't', 's')

tupla = list(reversed(('a', 'b', 'c', 'd')))
print(tupla)                                  # ['d', 'c', 'b', 'a']
"======================================================================================================================"



# iiwbwq4q9vlko8ytuq8wr56s2ea5ugs3d8yjdw7ebwgkslywinldxo7mprdo4ur85prniltq55vnzjfbec3zptoiwcm9hh4n4pmg
# rfind
# [ exclusivo string ] [ método prefixado ] [ similar ao método .index() ] [ método baseado em contagem indexada ]
# [ informador de última ocorrência de índice de dado (direita para esquerda) ]
# [ necessária soma + 1 para contagem normal (a partir do 1) (fora do escopo) ]
# [ não necessária soma + 1 para contagem indexada (a partir do 0) ]
"======================================================================================================================"
contexto = ('print', 'valor da variável', 'variável própria', 'variável nova')

string = '...0...0...7'
print(string.find('7') + 1)  # Quando foi a 1º ocorrência do dado [ '7' ] na variável [ string ] da <- para ->? [12]

string2 = 'Lucas_Farias*Santos@de$Sousa'.find('@') + 1
print(string2)               # 20

string3 = '__a___b'
string3 = string3.find('a') + 1
print(string3)               # 3

string4 = 'o3o xD :)'
string5 = string4.find(':') + 1
print(string5)               # 8

"Similaridade com o método [ .index() ]"
nome = 'Lucas Farias'
print(nome.find('s') + 1)   # 5
print(nome.index('s') + 1)  # 5
"======================================================================================================================"



# fwynlc3w5rek29sby3tdqki5ajn41ydjcjep7qdyq93npcvfcorjh4h5g6godkg9efmlnf51pqpoghnmm7cm8vrsxqehdwi2iukw
# rmdir
# [ 1 arg = string caminho da pasta + nome da pasta incluida ] [ removedor de pasta ]
# [ gerador de OsError caso pasta não vazia ] [ caso pasta não vazia, deletar arquivo/pasta um por um ]
"======================================================================================================================"
from os import rmdir, remove

# Supondo que haja no desktop uma pasta chamada [ pasta ] com um arquivo de texto chamado [ a.txt ]
remove('C:\\Users\\Lucas\\Desktop\\pasta\\a.txt')  # Será preciso deletar o arquivo primeiro
rmdir('C:\\Users\\Lucas\\Desktop\\pasta')          # Quando a pasta estiver vazia, ela pode ser deletada

# Supondo que haja no desktop uma pasta chamada [ pasta ] com outra pasta chamada [ pasta0 ]
rmdir('C:\\Users\\Lucas\\Desktop\\pasta\\pasta0')  # Será preciso deletar a pasta interna primeiro
rmdir('C:\\Users\\Lucas\\Desktop\\pasta')          # Quando a pasta matriz estiver vazia, ela pode ser deletada
"======================================================================================================================"



# lipwlb7m4kqr6ftjhbngzyswr17r569ywdznmc3bkphpw1ly6qn3kf8svctazve4kvw9pcutovfqz7epd41or9u8m6qcx3wlhlsu
# round
# [ aproximador de números inteiros ] [ critério para menos <= 5 <= para mais ] [ redutor de casas decimais ]
"======================================================================================================================"
contexto = ['print', 'valor da variável', 'variável própria', 'variável nova']

flutuante = 115.77  # valor acima da metade de 1 [ + 1 ]
flutuante2 = round(flutuante)
print(flutuante2)   # 116

flutuante = 115.49  # valor abaixo da metade de 1 [ - 1 ]
flutuante2 = round(flutuante)
print(flutuante2)   # 115

# Redutor de casas decimais
flutuant3 = 115.7844
print(round(flutuante3, 2))  # 115.78
"======================================================================================================================"



# xk8vmepy82jv4spuo7rmjunuxbutogq4fgoyoolepyw3xi94q5c1vyyeoz9gg7o15f7jfuowlu3axz4uuioq9vu9dcmgyx6b8x7j
# saída de dados
# [ %s {} f{} = caracteres especiais com ou sem letra para adição de texto ] [ usada em contexto normal ou em input ]
"======================================================================================================================"
# CONTEXTO DE INPUT % COM UM ARGUMENTO
nome = input('Qual o seu nome? -> ')
print('Obrigado, %s' % nome)

# CONTEXTO NORMAL % COM MÚLTIPLOS ARGUMENTOS
nome, sobrenome = 'Lucas', 'Farias'
print('Olá, %s %s' % (nome, sobrenome))

# CONTEXTO INPUT {} COM 1 ARGUMENTO
nacionalidade = input('Qual a sua nacionalidade?')
print('Legal, você é {}'.format(nacionalidade))

# CONTEXTO NORMAL {} COM MÚLTIPLOS ARGUMENTO
animal, pessoa = 'rato', 'rei'
print('O {} roeu a roupa do {} de Roma'.format(animal, pessoa))

# CONTEXTO DE INPUT f{} COM UM ARGUMENTO
idade = input('Qual a sua idade?? ->')
print(f'Certo, {idade} anos de idade')

# CONTEXTO NORMAL f{} COM MÚLTIPLOS ARGUMENTOS
print(f'Cala a boca, {nome.upper()}, e você também, {"-".join(sobrenome)}')
"======================================================================================================================"



# 9p772unfq9ekiudcb9o3tjqa65ha97h1ackwmuqq7dzuclyfx3m7dv2jg2q51ybwfhi4xxui6r1txxir8axeekyjud2dslzgdukv
# scandir [ similar listdir ] [ métodos aninhados ]
# [ 1 arg = string do caminho] [ sistema operacional ] [ gerenciamento de arquivos ]
# [ listador de arquivos em diretório ] [ gerenciamento indexado de dados ]
# [ métodos aninhados para obtenção de informações restritas ]
"======================================================================================================================"
from os import scandir

local = tuple(scandir('C:\\Users\\Lucas\\Desktop'))
print(local)

print(local[1].inode())       # 41376821576473041
print(local[1].is_dir())      # False
print(local[1].is_file())     # True
print(local[1].is_symlink())  # False
print(local[1].name)          # Downloads.lnk
print(local[1].path)          # C:\Users\Lucas\Desktop\Downloads.lnk
print(local[1].stat)          #
print(local[1].close())       #
"======================================================================================================================"



# todo há algo errado
# qfhfl3b4lo2hdf87klpemwks3za8e9bb1tdiooiy5zqwogyr6sbh62ljme3o1jrnh5klmf16cr6w51bq5hwfsp72thewbhmupz8p
# seek
# [ percorredor de caracteres em texto ] [ restringidor de vizualização ] [ função de retornar à 1ª linha ]
"======================================================================================================================"
# contexto = ('pós-variável',)
#
# arquivo = open("seek.txt", "r")
# arquivo.seek(5)        # Conforme a cursor desloca 6 casas, as casas percorridas ficam escondidas
# print(arquivo.read())  # [ Nome: Lucas ] torna-se [ Lucas ], pois "Nome: " possui comprimento [6]
# arquivo.seek(0)        # Retorna à linha 1
#
# "Outra forma:"
# arquivo2 = arquivo.read().split()
# print(arquivo2)              # ['Nome:', 'Lucas', 'Idade:', '27', 'Nacionalidade:', 'brasileiro']
# palavra_removida = arquivo2.pop(arquivo2.index('Nome:'))
# print(arquivo2)              # ['Lucas', 'Idade:', '27', 'Nacionalidade:', 'brasileiro']
# print(palavra_removida)      # Nome:
"======================================================================================================================"



# wu7ixqr1us45wdi92rjbff76hoq7ttgbatdbc4bb2skbolnpa6wgcqnajg1hqour99le4kzm1vjwd711av4qf2f8rijqyxk2ku9g
# setUp & tearDown
# [ importação mandatória ]
# [ criação de módulo mandatória ]
# [ importação restrita de módulo com nome da classe interna mandatória ]
# [ método criador de objeto de instância com self para uso em métodos de teste ]
# [ teste com POO (não sei dizer se programação estruturada serve para esses métodos) ]
"======================================================================================================================"
from unittest_ex_estrutural import TestCase, main     # from módulo import dois métodos mandatórios
from doc_classe_android import Android  # from módulo import nome da classe interna


############
"Observação"
# Usa-se [ tearDown ] ao final de cada método de teste
# De acordo com o professor, é util para:
#    -> excluir dados
#    -> fechar conexões com banco de dados
"    -> Utilidade não compreendida até o momento"
############


class AndroidTestes(TestCase):

    def setUp(self):
        self.xenon = Android('Xenon', 70)  # objeto de instância criado dentro do método [ setUp ]
        self.calu = Android('Calu', 67)
        print('setUp foi executado')

    def test_recarregar(self):
        self.xenon.recarregar()  # objeto de instância chamado com [ self. ] mandatório
        self.assertEqual(self.xenon.bateria, 100)

        "Sem usar o método [ setUp ]"
        # xenon = Android('Xenon', 70)
        # xenon.recarregar()
        # self.assertEqual(xenon.bateria, 100)

    def test_reproduzir_apelido(self):
        self.assertEqual(self.calu.reproduzir_apelido(), 'Olá, humano, meu apelido é CALU')
        self.assertEqual(self.calu.bateria, 66, 'A bateria deveria ter diminuído em 1')

        "Sem usar o método [ setUp ]"
        # calu = Android('Calu', 67)
        # self.assertEqual(calu.reproduzir_apelido(), 'Olá, humano, meu apelido é CALU')
        # self.assertEqual(calu.bateria, 66, 'A bateria deveria ter diminuído em 1')

    def tearDown(self):
        print('tearDown foi executado')


if __name__ == '__main__':
    main()
"======================================================================================================================"



# e7t2vqoka9is4ojnmeulaodpde7f7vpbn6bqvqufwdd8q29qnqwjzyccfuxmvu15yzw5caf7wnjnxc1amg5vl4janhw79cw8ryom
# shuffle
# [ importação mandatória ] [ desorganizador aleatório de dados em classes iteráveis ] [ 1 arg = itera lit/var ]
"======================================================================================================================"
contexto = ['pós-variável']
from random import shuffle

lista = ['...', False, 2020, '_'.join('Lucas'[::-1]), '{}'.format([dados for dados in range(1, 8)])]
shuffle(lista)
print(lista)  # [2020, 's_a_c_u_L', False, '[1, 2, 3, 4, 5, 6, 7]', '...']
"======================================================================================================================"



# 7dt8lkriaqgxxr1grcwvrxnp3o1ybjxux7ep8tglbut9www2ie9nkxyce226dbwpwsbdxop23cqjdtvoyhfdtx69ahpwyqqwy9bi
# sleep
# [ importação mandatória ] [ criador de intervalos entre etapas de algoritmo ] [ 1 arg = int/float ]
# [ recurso incompatível se contido no mesmo escopo de print ou variável ]
"======================================================================================================================"
contexto = ('pós-variável',)
from time import sleep

"Uso apropriado do método [ sleep() ]"
#########################################
print('Processando seu pedido'), sleep(1)
print('aguarde um instante...'), sleep(1)
print('...'), sleep(1)
print('Progresso: 22%'), sleep(2)
print('Progresso: 67%'), sleep(3)
print('Obrigado, por esperar')
#########################################

"Uso estranho do método [ sleep() ] [ anterior a um print() ]"
###################################################
sleep(1), print('Processando seu pedido'), sleep(1)
###################################################

# OBS: [ sleep() ] tem como valor [ None ], por isso, seu uso simultâneo com outros recursos, não é recomendável
# OBS: O que é recomendável? usá-lo posteriormente a outro recurso (uso externo)

"[ sleep() ] usado incorretamente em [ print() ] [ uso interno ]"
##################################################################################################
print('Eu sou o método [ sleep() ], e crio intervalos. Esse intervalo foi de 1 segundo', sleep(1))
##################################################################################################

"[ sleep() ] usado corretamente em [ print() ] [ uso externo ]"
##################################################################################################
print('Eu sou o método [ sleep() ], e crio intervalos. Esse intervalo foi de 1 segundo'), sleep(1)
##################################################################################################

"[ sleep() ] usado incorretamente em formatação de string"
############################################
texto = """
Você não pode usar [ sleep() ] com chaves {}
Sleep[ () ] {} é imcompatível com formatação
""".format(sleep(1), sleep(1))
print(texto)
############################################

"[ sleep() ] usado corretamenta em formatação de string"
############################################################
print("Você não pode usar [ sleep() ] com chaves"), sleep(1)
print("[ sleep() ] é imcompatível com formatação"), sleep(1)
############################################################
"======================================================================================================================"



# 9ichmxf4n25zwmvn27dkinbnuekylg2uzevh9sdbe4wxkfwhusz9uwbkjec3gz3zc97m62vlq48n55gze72c562hmueotdakn9n3
# sort
# [ exclusivo lista ] [ organizacional menor para maior ] [ hierarquia de caixa alta sobre baixa ] [ parâmetro vazio ]
# [ variedade de classes intelorável ]
"======================================================================================================================"
contexto = ('pós variável',)

lista = """
        Olá, Lucas Farias Santos,
        Sua senha de login foi alterada. Se você acha que isso seja um erro, clique no botão abaixo para acessar
        nosso portal de suporte
        """.split()

lista.sort()  # ordenação alfabética normal iniciada após dados em caixa alta
print(lista)
# ['Farias', 'Lucas', 'Olá,', 'Santos,', 'Se', 'Sua', 'abaixo', 'acessar', 'acha', 'alterada.', 'botão',
# 'clique', 'de', 'de', 'erro,', 'foi', 'isso', 'login', 'no', 'nosso', 'para', 'portal', 'que', 'seja', 'senha',
# 'suporte', 'um', 'você']

lista2 = [89, 92, 25, 7, 29, 91, 35, 85, 2, 90, 63, 3, 32, 71, 21, 98, 82, 52, 72, 79, 93, 38, 19, 62, 95, 67]
lista2.sort()
print(lista2)  # [2, 3, 7, 19, 21, 25, 29, 32, 35, 38, 52, 62, 63, 67, 71, 72, 79, 82, 85, 89, 90, 91, 92, 93, 95, 98]

lista3 = ['a', True, 7j, ({'conjunto'}), 0.0]
lista3.sort()
print(lista3)  # TypeError: '<' not supported between instances of 'bool' and 'str'
"======================================================================================================================"



# 366gxg42bbnla8cotbf29kjv6e74emcnbwl9vkqurbl9c1d2k74obgazhi9hkbiwhc27izwy2tl146h7wwdx1qcb4ad4lnxze5f3
# sorted
# [ 1/2 args = iterador, argumento chave com/sem função lambda ] [ criador padrão de lista ] [ uso híbrido em coleções ]
# [ dados de mesma classe mandatório ] [ resultado da organização de ocorrência ao final da coleção ]
# [ hierarquia caixa alta e baixa ] [ organização numérica do menor para maior ]
# [ organização numérica do maior para o menor com argumento chave reverse=True ]
"======================================================================================================================"
contexto = ['print', 'valor da variável', 'variável própria', 'variável nova']

"O que acontece se for tentado o uso de [ sorted() ] com coleções contendo classes distintas? "
# TypeError: '<' not supported between instances
# lista3 = ['a', True, 7j, ({'conjunto'}), 0.0]
# lista3 = sorted(lista3)
# print(lista3)

# hierarquia caixa alta e baixa
# dados de mesma classe mandatório
lista = """
        Olá, Lucas Farias Santos,
        Sua senha de login foi alterada. Se você acha que isso seja um erro, clique no botão abaixo para acessar
        nosso portal de suporte
        """.split()

lista2 = sorted(lista)
print(lista2)
# ['Farias', 'Lucas', 'Olá,', 'Santos,', 'Se', 'Sua', 'abaixo', 'acessar', 'acha', 'alterada.', 'botão', 'clique',
# # 'de', 'de', 'erro,', 'foi', 'isso', 'login', 'no', 'nosso', 'para', 'portal', 'que', 'seja', 'senha', 'suporte',
# # 'um', 'você']

# organização numérica do menor para maior
lista3 = sorted([89, 92, 25, 7, 29, 91, 35, 85, 2, 90, 63, 3, 32, 71, 21, 98, 82, 52, 72, 79, 93, 38, 19, 62, 95, 67])
print(lista3)  # [2, 3, 7, 19, 21, 25, 29, 32, 35, 38, 52, 62, 63, 67, 71, 72, 79, 82, 85, 89, 90, 91, 92, 93, 95, 98]

# organização numérica do maior para o menor com argumento chave reverse=True
lista4 = sorted(lista3, reverse=True)
print(lista4)  # [98, 95, 93, 92, 91, 90, 89, 85, 82, 79, 72, 71, 67, 63, 62, 52, 38, 35, 32, 29, 25, 21, 19, 7, 3, 2]

# [ sorted() com 2 argumentos: iterador, argumento chave key=len [ organização por comprimento de dados ]
lista5 = lista
print(list(sorted(lista5, key=len)))
# ['de', 'Se', 'um', 'no', 'de', 'Sua', 'foi', 'que', 'Olá,', 'você', 'acha', 'isso', 'seja', 'para', 'Lucas', 'senha',
# 'login', 'erro,', 'botão', 'nosso', 'Farias', 'clique', 'abaixo', 'portal', 'Santos,', 'acessar', 'suporte',
# 'alterada.']

"[ sorted() ], quando influenciada por função lambda e operador relacional, pode gerar ordenação estranha"
"O que isso significa?"
# Por exemplo, o que foi configurado como ação em [ sorted() ] gera retorno ao final, não ao começo

# 1. Cria-se uma variável [ lista6 ] que será influenciada pelo [ sorted() ]
# 2. A variável [ lista7 ] recebe [ sorted() ] + função lambda, para gerar uma organização alternativa em [ lista6 ]
# 3. [ lista7 ] pede como organização, cada dado (cada palavra) em [ lista6 ] cujo 1º indice seja = 'p'
# 4. É esperado que a condição da organização passada, traga esses dados à frente da coleção
# 5. Porém, o comportamento é o inverso
# 6. Mas, é possível reverter isso com o argumento chave [ reverse=True ], como é feito na variável [ lista8 ]
# 7. [ sorted ] encontra-se influenciado por [ casting tupla ] apenas por redução de armazenamento [ não é mandatório ]
lista6 = "Se você acha que isso seja um erro, clique no botão abaixo para acessar nosso portal de suporte".split()
lista7 = tuple(sorted(lista6, key=lambda cada_dado: cada_dado[0] == 'p'))
lista8 = tuple(sorted(lista6, key=lambda cada_dado: cada_dado[0] == 'p', reverse=True))
print(lista7)
print(lista8)

# ('Se', 'você', 'acha', 'que', 'isso', 'seja', 'um', 'erro,', 'clique', 'no', 'botão', 'abaixo', 'acessar', 'nosso',
# 'de', 'suporte', 'para', 'portal')

# ('para', 'portal', 'Se', 'você', 'acha', 'que', 'isso', 'seja', 'um', 'erro,', 'clique', 'no', 'botão', 'abaixo',
# 'acessar', 'nosso', 'de', 'suporte')

lista9 = [{'nome': 'Lucas', 'idade': 27}, {'nome': 'Santos', 'idade': 39}, {'nome': 'Sousa', 'idade': 71}]
print(sorted(lista9, key=lambda cada_valor: cada_valor['idade']))
# [{'nome': 'Lucas', 'idade': 27}, {'nome': 'Santos', 'idade': 39}, {'nome': 'Sousa', 'idade': 71}]
"======================================================================================================================"



# q6huxei2p3gfufbcfvrof8zxyaxmlgc5haylgl8egssrxld986jusy72m6lh723ve7jqg4ptrjwdvofn98r6mb6o1a69m3mma5h4
# split()
# [ exclusivo string ] [ 0/1 arg = vazio/arg string separador ] [ conversão textual para lista ]
# [ arg padrão vazio = separação por espaço ]
"======================================================================================================================"
contexto = ('print', 'valor da variável', 'variável própria', 'variável nova')

string = 'string'
print(string.split())  # ['string']

string2 = 'string string2'.split()
print(string2)         # ['string', 'string2']

string3 = 'Muitos não sabem, mas não há inferno, pois o inferno, é a própria terra'
string3 = string3.split(',')
print(string3)         # ['Muitos não sabem', ' mas não há inferno', ' pois o inferno', ' é a própria terra']
"======================================================================================================================"



# 2ssi4r7y9ory5ya1wnwdt11sxer49ioho4hc5fyu3two974pcqvbnv8lu5owhzfr2bpolii99qcgwru917nnago3d1b9l4ncwn6s
# strftime
# [ importação mandatória ] [ método prefixado ] [ tempo em formato de texto/string ]
# [ método com variedade de argumentos muito extensa ] [ método secundário do método datetime ]
"======================================================================================================================"
contexto = ('print', 'valor da variável')
from datetime import datetime

print(datetime.now().strftime('%d/%m/%Y'))         # 14/05/2020     # demonstração em print

data_brasil = datetime.now().strftime('%d/%m/%Y')  # Padrão brasileiro de data
print(data_brasil)                                 # 14/05/2020

data_usa = datetime.now().strftime('%Y/%m/%d')     # Padrão americano de data
print(data_usa)                                    # 05/14/2020

# MOSTRAR DATA DE FORMA ALTERNATIVA (sem strftime)
data_usa_alternativa = str(datetime.now()).split()[0]  # Padrão americano usando método [ datetime(1, 2, 3, 4, 5, 6) ]
print(data_usa_alternativa)  # 2020-05-14

# MOSTRAR DATA COM O NOME DO MÊS
data_mostrando_mes = datetime.today().strftime('%B/%d/%Y')
print(data_mostrando_mes)    # May/14/2020
"======================================================================================================================"



# txohkzszmlrxdu2395m8tt6jve8sylzw1oufdlh894sslmptfd4cbi98mybwdlv898pbxtnollfls72acddkf2ykqopk6cqsik9d
# strptime
# [ importação mandatória ] [ conversor de data string para padrão do método datetime() ]
# [ método aninhado do método datetime() ]  [ 2 args = data string, data string datetime ]
# [ recomendável saber os formatos de string datetime e suas ordens de posicionamento ]
"======================================================================================================================"
contexto = ('print', 'variável nova')
from datetime import datetime

# 1º e 2º argumentos precisam estar na mesma ordem
# 16   = dia     formatação de data     16   = '%d'
# 07   = mês     formatação de data     07   = '%m'
# 1992 = ano     formatação de data     1992 = '%Y'
data = datetime.now().strptime('16/07/1992', '%d/%m/%Y')

print(type(data))  # <class 'datetime.datetime'>
print(data)        # 1992-07-16 00:00:00
print(data.day)    # 16
print(data.month)  # 7
print(data.year)   # 1992
"======================================================================================================================"



# 4f6zzryjrx7zybhdie4mfqfny9vr8trq8kd5xlmvprnrzifmotalkk4q8cvhmt3aqppp27qygvc1xcs3ml1fxcyftifsbaud8fq4
# sum
# [ somador de dados não iteráveis em classes iteráveis ] [ intolerância à não unicidade de classe numérica ]
# [ float prioridade sobre int ]
"======================================================================================================================"
contexto = ('print', 'valor da variável', 'variável própria', 'variável nova')

lista = sum([1, 2, 3, 4, 5])
print(lista)  # 15

"Caso haja mistura de dados numéricos [ int and float ]"
"Valor torna-se flutuante [ casting pode corrigir ]"
########################################################
lista3 = [1, 2, 3, 4, 5, 6.0]
print(sum(lista3))       # 21.0
print(int(sum(lista3)))  # 21
########################################################

"Caso não haja unicidade de classe numérica [ TypeError ]"
##########################################################
# lista2 = sum([1, 2, 3, 4, 5, 'Lucas'])
# print(lista2)
##########################################################
"======================================================================================================================"



# emfls8gbrjmde82lbrqmgienlaznh8l5y3kqj6o6l93jemwg4pn2o2unqyqo1futh28gqcgdwj8b3pjc5uawitpgngltf8w9ujre
# time
# [ importação mandatória ] [ criador de hora ] [ 3 args obrigatórios = hora, minuto, segundo ]
# [ 4 args opcional = hora, minuto, segundo, microsegundo ] [ argumento chave opcional ]
# [ acesso aos dados de hora por notação ponto com ou sem presença de argumento chave ]
"======================================================================================================================"
from datetime import time

hora = time(hour=7, minute=12, second=50, microsecond=10777)
print(time(12, 12, 12))  # Exemplo de hora em print e sem argumento chave        # 12:12:12
print(hora)              # Exemplo de hora em variável e com argumento chave     # 07:12:50.010777
print(hora.hour)
print(hora.minute)
print(hora.second)
print(hora.microsecond)
"======================================================================================================================"



# uhhmfkkfn4cs6uwdvnyoqlmeujvkkcxphpqoq4j7z7a1xfx636q9j4yqp5p4x5hydqvrzbjfw7zahlf5t61n4yoezhrkcihg67h5
# timedelta
# [ importação mandatória ] [ calculador de datas ]
"======================================================================================================================"
from datetime import datetime, timedelta

data_compra = datetime.now()
print(data_compra)       # 2020-05-12 12:07:01.388718
prazo_vencimento = timedelta(days=30)
print(prazo_vencimento)  # 30 days, 0:00:00
data_vencimento = data_compra + prazo_vencimento
print(data_vencimento)   # 2020-06-11 12:07:01.388718
"======================================================================================================================"



# g64z8l9m8e77znqrll4ylo7z8nlnsp5hi9cge3dohbvfgurlc8b98k2crz9q1vgvclfixx6jfxqdn3ep2yubu4xfjeium2eikhai
# timeit
# [ importação mandatória ] [ calculador de tempo de execução de códigos ] [ código em formato de string mandatório ]
# [ 2 args = stmt= código, number=nº de repetições ] [ formas diferentes ]
"======================================================================================================================"
from timeit import timeit

##############################################################################################
"Se for usado print() junto ao código: mostra-se o tempo de execução + o código repetidamente"
"Caso contrário                      : mostra-se o tempo de execução"
##############################################################################################

#############################################
"Forma 1 [ timeit ] no [ valor da variável ]"
var = timeit(stmt="print(tuple((str(cada_dado) for cada_dado in range(1, 100 + 1))))", number=10)
print("Forma 1 [ valor da variável ]\n", var)
#############################################

#################################
"Forma 2 [ timeit ] em [ print ]"
var2 = "print(tuple((str(cada_dado) for cada_dado in range(1, 100 + 1))))"
print("Forma 2 [ print ]\n", timeit(stmt=var2, number=10))
#################################

#######################################################################
"Note que em caso de o código ser uma string, deve-se ter duas strings"
var3 = timeit(stmt="'Lucas Farias Santos de Sousa'", number=100)  # stmt também precisa de aspas
print(var3)

var4 = 'print("Lucas Farias Santos de Sousa")'  # Sem print -> '"Lucas Farias Santos de Sousa"'
print(timeit(stmt=var4, number=100))
#######################################################################
"======================================================================================================================"



# laluz4srndehw7jezba46qxv98j9bh61lxm4ukfjwiheik59g9jzbng35nba4xuured1fecjm1jwgoaje8v5kzsvbsazq3pdqh7x
# title
# [ exclusivo string ] [ aplicador de cacha alta a cada novo separador que não for letra ] [ parâmetro vazio ]
"======================================================================================================================"
contexto = ('print', 'valor da variável', 'variável própria', 'variável nova')

nome_composto = 'super-homem'        # nesse contexto, o separador é "-", o que vier após o separador, terá cacha alta
print(nome_composto.title())         # Super-Homem

nome = 'alfredo adolfo'.title()      # quem é o separador? barra de espaço
print(nome)                          # Alfredo Adolfo

dicio = {'entidade': 'deus'}
dicio = dicio['entidade'].title()    # se não há separador, então apenas a letra inicial é posta em cacha alta
print(dicio)                         # Deus

tupla = (cada_indice.title() for cada_indice in ('país:brasil', 'país#suécia', 'país/canadá'))
print(tuple(tupla))                  # ('País:Brasil', 'País#Suécia', 'País/Canadá')
"======================================================================================================================"



# todo Algo está errado
# nnzv35ousqyp1yavn2f18y2j935e28n7kwlcgsw67nog3a8g3nipw2x1pylrjqmw96pn3u5po151tc3l2w4hwfhhjp85j73lrp5s
# translate
# [ importação mandatória ] [ tradutor de var/lit string ] [ biblioteca pesada ] [ 1 arg = argumento-chave=string ]
# [ passagem de string da linguagem no formato correto mandatório ] [ razão da ineficiência = consulta online ]
"======================================================================================================================"
# contexto = ('print', 'valor da variável', 'variável própria', 'variável nova')
# from textblob import TextBlob
#
# print(TextBlob('translate it into portuguese').translate(to='pt-br'))  # traduza para o português
#
# var = TextBlob('Eu sou um programador').translate(to='eng-us')
# print(var)                                                        # I am a programmer
#
# string = 'Eu reconheço a verdade quando a vejo!'
# traduzir_string = TextBlob(string).translate(to='eng-uk')
# print(traduzir_string)                                            # I recognize the truth when I see it!
"======================================================================================================================"



# 5fu8hcnzl8j77ya2iuda62xpsqiwax3ybgt922v4hr42dau22i3jxvcwa3d6l6792nxyfenjofgfc832wdzzrr3rn39jmcwlb3p9
# trunc
# [ importação mandatória ] [ 2 args = int/flut ] [ resto de divisão pythônica ] [ arredondamento bruto ]
"======================================================================================================================"
contexto = ['print', 'valor da variável', 'variável própria', 'variável nova']
from math import trunc

inteiro = 2020 / 9
inteiro2 = trunc(inteiro)
print(inteiro2)         # 224

print(trunc(2020 / 9))  # 224
"======================================================================================================================"



# b2vtopmrum6xsmhbme4bqxggjdchlbcqd1upici8s7poo4175i18s6n389z1573a9882b1k8wopiwxc6cckqhw7l7mo46wos6fow
# try & except
# [ tratamento de erro Pythônico ] [ dupla dependência ] [ escopo local ]
# [ var integrada para nomeação de erro ] [ erro nomeado gerador de erro do sistema ]
# [ erros customizados ] [ tratamento múltiplo de erros ] [ agrupamento de erros em tupla ]
"======================================================================================================================"
try:                                 # [ try & except ] dependência mútua
    len(2020)                        # Possível erro a ser tratado [ interno ao escopo local ]
except TypeError as err:             # var integrada [ err ] para nomeação de erro
    print('Erro do sistema: ', err)  # erro nomeado gerador de erro do sistema
    print('Erro customizado: [ len() ] não trabalha com a classe [ inteiro ]')
                                     # Erro do sistema:  object of type 'int' has no len()
                                     # Erro customizado: [ len() ] não trabalha com a classe [ inteiro ]


# Tratamento múltiplo de erros
try:
    len(2020)
except NameError:
    print('Agrupamento de erro')
except TypeError as a:
    print('Agrupamento de erro')
except ValueError as b:
    print('Agrupamento de erro')

# Agrupamentos de erro em tupla só é recomendável se for feito um tratamento bem genérico
# A melhor saída é tratar erros individualmente
try:
    len(2020)
except (NameError, TypeError, ValueError):
    print('Agrupamento de erros')
"======================================================================================================================"



# ml3edls4z6553molgufp6x8kbutcd5b7a561s2c6uccr342xkm2rvcgzy9jedr5qw7gz6xbzat1m8qjun91hsvzf8e652l5daw5t
# type
# [ 1 arg = lit/var ] [ retornador de classe ] [ print dependente ]
"======================================================================================================================"
contexto = ('print',)
from datetime import datetime

dicio = {'nome': 'Lucas'}

hoje = datetime.today()
data = datetime(year=hoje.year, month=hoje.month, day=hoje.day, hour=hoje.hour, minute=hoje.minute, second=hoje.second)
nascimento = datetime(1992, 7, 16)
tempo_de_vida = hoje - nascimento


def var():
    pass

with open('xyz.txt', 'a+') as algo:
    pass


class Celular:
    def __init__(self, nome):
        self.__nome = nome

asus = Celular('Asus')

print(type(not True))              # <class 'bool'>
print(type({'conjunto'}))          # <class 'set'>
print(type({'dicionário': None}))  # <class 'dict'>
print(type(2020.0))                # <class 'float'>
print(type(2020))                  # <class 'int'>
print(type([2020]))                # <class 'list'>
print(type(range(1, 2021)))        # <class 'range'>
print(type(None))                  # <class 'NoneType'>
print(type(''))                    # <class 'str'>
print(type(('',)))                 # <class 'tuple'>
print(type(var))                   # <class 'function'>
print(type(algo))                  # <class '_io.TextIOWrapper'>
print(type(asus))                  # <class '__main__.Celular'>
print(type(dicio.keys()))          # <class 'dict_keys'>
print(type(dicio.values()))        # <class 'dict_values'>
print(type(data))                  # <class 'datetime.datetime'>
print(type(tempo_de_vida))         # <class 'datetime.timedelta'>
"======================================================================================================================"



# ds7j7vkhahf5345u3jmn6ci177st7smu1ap1t5emfnbu3j3n81dqw65kurbrlmdc8nsq2m35yybjuea69dbjpsfxk6nmt4dgbf8s
# type hinting
# [ informador de classe em parâmetro (função) ] [ facilitador de vizualização de classe pedida em parâmetro ]
# [ função com type hinting é geradora de anotação ]
"======================================================================================================================"


def cacha_alta(frase: list) -> list:  # Explicitar tipos de dados é chamado de [ annotations = anotações ]
    var = [str(each_data).upper() for each_data in frase]
    return var

print(cacha_alta(['nome', True, 0, {'Brasil', None}]))  # ['NOME', 'TRUE', '0', "{'BRASIL', NONE}"]

"[ type hinting ] torna possível o acesso a anotação"
print(cacha_alta.__annotations__)
notas = cacha_alta.__annotations__
print(notas)  # {'frase': <class 'list'>, 'return': <class 'list'>}
"======================================================================================================================"


# h7pvm3vk1kemd7ro2bbb7vyewejidym3dam6nyljjf4evo4hicuh2nw5kjzm935z79md15fdmpw738uo59d9btrn1sx7s4rh2poo
# type hinting (em comentário)
# [ explicitação de tipo de classe em parâmetro fora do parâmetro ]
"======================================================================================================================"
"O correto e fazer [ type hinting ] no parâmetro, mas em comentário pode ser uma forma alternativa"


def raiz(valor):
    # type: (int) -> float             # dado de tipagem único -> tipagem do retorno
    return valor ** 0.5


def dados(nome='', idade=0, atleta=None):
    # type: (str, int, bool) -> tuple  # dados de tipagem múltiplos -> tipagem do retorno
    return nome, idade, atleta

print(dados('Lucas', 27, True))

"Exemplo de sintaxe de tipagem muito incomum, porém possível"


def dados_estranho(
        nome='',  # type: str
        idade=0,  # type: int
        atleta=None  # type: bool
):  # type: (...) -> tuple
    return nome, idade, atleta
print(dados_estranho('Alfredo', 90, False))

dados_pessoa = ('Túlio', 40, True)  # type: tuple  # Tipagem de variável por comentário
"======================================================================================================================"



# n89l7emhbg3926z6ogvssdcmt6af47xomkoxvq2ze5qtoti8p38pblcticxyettaa1h8bmmd3ws5ohrpdlbfuwqvb9maa1x282j8
# typewrite
# [ importação mandatória ] [ automação para escrita ] [ escrita instantânea // intervalada ]
"======================================================================================================================"
from pyautogui import typewrite

typewrite('Lucas Farias Santos de Sousa')       # string [ impressão instantânea ]
typewrite('Lucas Farias Santos de Sousa', 0.2)  # string [ impressão intervalada ]
"======================================================================================================================"



# 8mwcm8n7drphbatqgb27btzn5c2e9mtw3tilm4i6d9vkprrkkgfa9kumab1xihdrkse14p3dplfde1btoeiwlt4tls3vmglfrke1
# typing
# [ importação mandatória ] [ forma alternativa de tipagem de dados em coleções ] [ tipagem mais ampla ]
"======================================================================================================================"
from typing import Dict, List, Set, Tuple

dados_individuo: Dict[str, str] = {'nome': 'Jânio', 'idade': '62', 'atleta': 'False'}
dados_individuo_lista: List[str] = ['Lucas', '27', 'True']
raizes: Set[int] = {27, 44, 212, 22.0}
medidas: Tuple[float, int, float] = (22.5, 12, 24.44)  # A ordem precisa ser seguida
print(dados_individuo)
print(dados_individuo_lista)
print(raizes)
print(medidas)
"======================================================================================================================"



# hv9t7lrfiicw6ioqfle4cxfqk4v1dtwo5r381mnrr28nln25lgx3axap4az6fm6ep84magxyccmcrtctg5u8tnv7ityg5dft64gu
# underline
# [ separador pythônico de casas decimais ] [ substituidor de ponto ] [ ignorado em impressão ]
"======================================================================================================================"
inteiro = 2_892_458
print(inteiro)    # 2892458

flutuante = 2_892_458.999
print(flutuante)  # 2892458.999
"======================================================================================================================"



# da8s18mku5brfqsc6sz4lyj8fua3542vnsljf9at623eqhspcyaj99qkh8z175f97eerexu91qc86p4yt47z3vqi4d8es8cr456p
# uniform
# [ importação mandatória ] [ 2 args = complex/int/float ] [ gerador/retornador de flutuante ] [ aleatório ]
# [ interação livre entre negativos e positivos ] [ interação livre entre classes numéricas diferentes ]
"======================================================================================================================"
contexto = ['print', 'valor da variável']
from random import uniform

conj = {uniform(1, 99), uniform(-99, 1)}
print(conj)  # {64.36773393350808, -60.377886858538744}

"Em caso de não haver argumentos necessários para o método"
var = uniform(1)  # TypeError: uniform() missing 1 required positional argument: 'b'
"======================================================================================================================"



# 1h9n56w7rxvqrbjv8csidnak5q6l5qpzx6pmw76k8j8tpiyslnxwdvjvgbob4uwbjkud2r435qclgfxwapzw2wsoxmro6plvmqmw
# union
# [ exclusivo conjunto ] [ união de dados entre conjuntos ] [ var matriz união var(s) alvo ] [ args múltiplos ]
"======================================================================================================================"
contexto = ['print', 'valor da variável', 'variável própria', 'variável nova']

conj = {'Lucas', 'Farias', 'Santos', 'de', 'Sousa'}
conj2 = {'Maria', 'do', 'Rosário', 'de', 'Fátima'}
conj3 = {'Maria', 'Flôr', 'Farias', 'Santos'}

conj3 = conj3.union(conj2, conj)
print(conj3)  # {'Farias', 'Fátima', 'do', 'Rosário', 'Lucas', 'Maria', 'Sousa', 'de', 'Flôr', 'Santos'}
"======================================================================================================================"



# yp66fcno62wxpbjnvgm2yicoao9w4xs1pexshz3cmcg3pwrui39o3q6jnvsnmrk3staqt1osm39shmle3z8yxewg4dn3qbeen8oy
# unittest
# [ importação mandatória ]
# [ criação de módulo mandatória ]
# [ importação restrita de módulo com função(ões) mandatória ]
# [ teste de códigos em função ] [ teste com função sem parâmetro, até agora desconhecida ]
"======================================================================================================================"
from unittest_ex_estrutural import TestCase, main

# 1. Cria-se uma classe [ recomenda-se mesmo nome do módulo/arquivo que será testado ]
# 2. A herança dessa classe criada é o método [ TestCase ]
# 3. No escopo da classe, recomenda-se chamar os métodos com [ test_ ] antes do seu nome real
# 4. Os métodos secundários [ assert ] do método [ TestCase ] são chamados com [ self ]
# 5. Os métodos [ assert ] passam pelo menos 2 args [ var da função com argumento nomeado, retorno esperado ]
# 6. O teste dos códigos mais recomendado é pelo terminal: [ ctrl + l ] e depois [ python nome_módulo.py -v ]

from doc_testagem import cumprimento, checar_hora_dia, adivinhar_quadrado


class Testagem(TestCase):

    # def test_comer(self):
    #     self.assertEqual(
    #         comer(alimento='batata-frita', nocivo=True),
    #         'O alimento batata-frita, vai matar você')
    #
    # def test_horas_sono(self):
    #     self.assertEqual(
    #         horas_sono(horas=7),
    #         'Eu dormi, mas ainda estou cansado')


    def test_cumprimento(self):
        # Exemplo com [ assertEqual ]
        # afirmar que é igual
        self.assertEqual(cumprimento(fala='êi'), '...')  # Afirmar que [ paâmetro êi ] retornará [ '...' ]

    def test_checar_hora_dia(self):
        # Exemplo com [ assertNotEqual ]
        # afirmar que não é igual
        self.assertNotEqual(checar_hora_dia(hora=8), 'tarde')  # Afirmar que [ parâmetro 8 ] não retorna [ 'tarde' ]

        "Exemplo com erro"
        # Exemplo com [ assertNotEqual ] afirmando algo errado, para mostrar 3º arg com mensagem alternativa
        # self.assertNotEqual(checar_hora_dia(hora=12), 'tarde', 'Eu me enganei')


    def test_adivinhar_quadrado(self):
        # Exemplo com [ assertTrue ]
        # afirmar que é True
        self.assertTrue(adivinhar_quadrado(valor=13, valor_quadrado=169), True)

        # Exemplo com [ assertFalse ]
        # afirmar que é False
        self.assertFalse(adivinhar_quadrado(valor=9, valor_quadrado=88), False)

if __name__ == '__main__':  # mandatório
    main()

"TestCase [ asserts mais comuns ]"
# https://docs.python.org/3/library/unittest.html
##########################################################
# Method                            # Checks that
"[ assertEqual(a, b)         ]"     # a == b
"[ assertNotEqual(a, b)      ]"     # a != b
"[ assertTrue(x)             ]"     # bool(x) is True
"[ assertFalse(x)            ]"     # bool(x) is False
"[ assertIs(a, b)            ]"     # a is b
"[ assertIsNot(a, b)         ]"     # a is not b
"[ assertIsNone(x)           ]"     # x is None
"[ assertIsNotNone(x)        ]"     # x is not None
"[ assertIn(a, b)            ]"     # a in b
"[ assertNotIn(a, b)         ]"     # a not in b
"[ assertIsInstance(a, b)    ]"     # isinstance(a, b)
"[ assertNotIsInstance(a, b) ]"     # not isinstance(a, b)
##########################################################
"======================================================================================================================"



# m4de9w1utj9wffp15ulllyuxwcedmtudle7wqxlfo6oifj7up5fi4lt25jp8pklt5aa786tocjkn4cgamnfsqqkavvbjpy6f13vw
# update ou [] =
# [ 2 args = chave & valor ] [ 2 formas ] [ exclusivo dicionário ] [ atualização/inserção de uma chave & valor ]
"======================================================================================================================"
contexto = ['pós-variável']

dicio = {'nome': ''}
print(dicio)                     # {'nome': ''}
dicio.update({'nome': 'Lucas'})  # atualização da chave ['nome']
print(dicio)                     # {'nome': 'Lucas'}
dicio.update({'idade': 27})      # inserção de nova [ chave ]
print(dicio)                     # {'nome': 'Lucas', 'idade': 27}
dicio['idade'] = 20              # atualização da chave ['idade']
print(dicio)                     # {'nome': 'Lucas', 'idade': 20}
dicio['ciclista'] = True         # inserção de nova [ chave ]
print(dicio)                     #  {'nome': 'Lucas', 'idade': 20, 'ciclista': True}
"======================================================================================================================"



# d8dkvs35gbvwm9rqymu6kpqp9y8fvu76wpaqlc554s2r72pwzmba41bkzabstbv5kzti2kqvr579v6p84iyo8ackt7trj7bddtvv
# upper
# [ exclusivo string ] [ parâmetro vazio ] [ caracteres em cacha alta absoluta ]
"======================================================================================================================"
contexto = ['print', 'valor da variável', 'variável própria', 'variável nova']

pais = 'BRasil'
print(pais.upper())                  # BRASIL

grito = 'aaaaaaa!'.upper()
print(grito)                         # AAAAAAA

frase = ['foda-se!']
frase = frase[0].upper()
print(frase)                         # FODA-SE!

tupla = (('nome'.upper().replace('NOME', 'NICK'), 'Lucas'.upper()[::-1]),)
print(tupla)                         # (('NICK', 'SACUL'),)
"======================================================================================================================"



# i8zvrcw76zve9feufyxmjwtur83zlpgu1mibjqm5nwvv59zapicmkgmgte7zsk2no4w2hdg6p78ntfuhrguqjhrzqpdhewtrqvnu
# values
# [ exclusivo dicionário ] [ ruptor de elo entre par chave & valor ] [ parâmetro vazio ] [ criador de lista de valores ]
# [ acesso à valores unicamente por casting ]
"======================================================================================================================"
contexto = ['print', 'valor da variável', 'variável própria', 'variável nova']

dicio = {'dados': {'nome': 'Lucas', 'idade': 27, 'ciclista': True}}
print(dicio['dados'].values())     # dict_values(['Lucas', 27, True])
dicio2 = dicio['dados'].copy().values()
print(dicio2)                      # dict_values(['Lucas', 27, True])

casting_para_acessar_dados = list(dicio['dados'].values())

print(casting_para_acessar_dados)     # ['Lucas', 27, True]
print(casting_para_acessar_dados[2])  # True

# Caso seja tentado chamada direta, retorna-se um erro
dados_de_dicio = dicio.values()
print(dados_de_dicio)              # dict_values([{'nome': 'Lucas', 'idade': 27, 'ciclista': True}])
print(dados_de_dicio['nome'])      # TypeError: 'dict_values' object is not subscriptable
print(dados_de_dicio[1])           # TypeError: 'dict_values' object is not subscriptable
"======================================================================================================================"



# ltmk74nqexbgskfz21hwlmesfo4zdtl7d3jdat7ffamdj8rkvqxee2tc8fh2dq8l1ev7uarpixvuuskgksurpdjzo4wjcw25rq1j
# verify [ instalação ] [ terminal = pip install passlib ]
# [ importação mandatória & complexa ] [ apelido recomendável ] [ uso híbrido = programação estruturada/ POO ]
"======================================================================================================================"
from passlib.hash import pbkdf2_sha256 as crypto


class Login:

    def __init__(self, key):
        self.key = crypto.hash(key, rounds=200_000, salt_size=16)


    def verificar(self, data_key):
        if crypto.verify(data_key, self.key):  # [ .verify(parâmetro, atributo) ] sendo usado como verficador
            return 'senha correta, você agora têm acesso'
        return 'senha incorreta'

pessoa = Login('password')
print(pessoa.verificar('password.'))  # senha incorreta
print(pessoa.verificar('password'))   # senha correta, você agora têm acesso


"Exemplo de [ verify() ] em programação estruturada"
senha = crypto.hash('alguma_coisa', rounds=200_000, salt_size=16)  # criação da senha com criptografia
print(senha)
verificar = crypto.verify('alguma_coisa.', senha)                  # verificação se senha é idêntica
print(verificar)                                                   # False
verificar2 = crypto.verify('alguma_coisa', senha)
print(verificar2)                                                  # True
"======================================================================================================================"



# mgbtx5715opwb8seobhqx16kt8vvyrn2u546mx6w7t6ghlvq8aiqnfn4i2w1nkuvs9bqeo82myg6b1n924svd53njaxchnn5zjwu
# wraps
# [ uso exato desconhecido ] [ corretor de docstring de função com decorador ]
"======================================================================================================================"
from functools import wraps


def f(par):
    @wraps(par)  # Se @wraps(par) estivesse ausente, a consulta de documentação abaixo seria incorreta
    def f2(*args, **kwargs):
        "doc string"
        return par(*args, **kwargs)
    return f2


@f
def f3():
    "doc string 2"
    return

print(f3.__doc__)  # Consulta à documentação da função [ f3() ]...
                   # Se @wraps(par) estivesse ausente...
                   # A consulta ao documento da função [ f3() ] chamaria a documentação do decorador, função [ f() ]
                   # Isso acontece, pois [ @f ] é um decorador da função [ f() ], e influencia a função [ f3() ]
                   # Por causa dessa influência, a função [ f3() ] acessa a documentação de forma erônia
                   # Mas a presença do @wraps(par) corrigi esse comportamento
"======================================================================================================================"



# tpxib2q6adeub6ycnc9pxrr3f2e4eyk6l6wccj2yhc1h67sqx8rq2t85bht4x6ag9it6z1tkl73l7kblyffqbfm6fsckvsmniiop
# write
# [ abertura e edição de arquivos ] [ escritor string em textos ] [ dependente de open() ] [ w ] [ a ]
# [ escrita de qualquer classe permitida contanto que haja casting string ]
"======================================================================================================================"

"[ write() ] funciona com ambas formas de abertura [ open() ] & [ with open() as var ]"
texto = open("open.txt", "w")  # Para escrita, é necessária a mudança da [ formatação ] de [ r ] para [ w ]
texto.write('1')            # Na formatação [ w ], a cada nova escrita, o texto anterior é [ sobescrito  ]
                            # ============= [ a ] ======================================== [ acumulativo ]

with open('with_open.txt', 'a') as doc:
    doc.write(str(['Lucas', 'Farias', 27, True, None]))
    doc.write(str('...'))
"======================================================================================================================"



# n9cyyedbrh8414typ953kjfvz472v7mtewktxm5ck5ka5zwkwf79besgpltkbamon49caumzimkhfi8c2hpys9crrf9t3ggyxqxu
# writer
# [ importação mandatória ] [ criação, abertura e escrita de arquivo em forma de lista ]
# [ 1 arg = variável do documento ] [ método .writerow([]) dependente ] [ criação de cabeçalho opcional ]
"======================================================================================================================"
from os import chdir
from csv import writer

chdir('c:\\users\\lucas\\desktop')
with open('writer.csv', 'w') as doc:  # [ writer ] trabalha com escrita, portanto usa-se [ w ]

    escrita_lista = writer(doc)       # [ writer ] recebe a variável do arquivo criado para escrita
                                      # no momento em que [ writer ] é criado, precisa-se do método [ .writerow([]) ]
                                      # [ .writerow([]) ] deve ter uma coleção dentro dele [ normalmente lista ]

    "Usa-se [ .writerow([]) ] para cada vez que se quer adicionar um novo conteúdo"
    escrita_lista.writerow(('nome', 'sobrenome', 'idade', 'nacionalidade'))  # Primeiro é criado um cabeçalho
    escrita_lista.writerow(('Lucas', 'Farias', 27, 'brasileiro'))            # Após, podem ser criados os dados
"======================================================================================================================"



# v4wtv8zfem3sh7954kx851nyr7zfjae2j8tez3qil7seipuzimh7pykg1zxi9y8zpizopuapfweyutl16ob2fgtx5q22bx7n4an5
# yield [ não consegui entender a utilidade ]
# [ palavra reservada ] [ função def & loop for dependente ] [ forma alternativa de return ] [ objeto de memória ]
# [ dependente de next() ] [ controlador de fluxo de iteração ] [ uso em função e uso simples ]
"======================================================================================================================"
def printer(itera):
    for each_data in itera:
        yield each_data

var = printer((1, 50, 27, 44, 1992, 0, 'Lucas'))

next(var)
next(var)
print(next(var))  # 27
next(var)
next(var)
next(var)
print(next(var))  # Lucas

def var():
    for each_data in 'Lucas Farias':
        yield each_data

nome = var()
print(next(nome))      # L
print(next(nome))      # u

# Exemplo fora de função que gera o mesmo resultado
var = iter((1, 50, 27, 44, 1992, 0, 'Lucas'))
next(var)
print(next(var))
"======================================================================================================================"



# eh9to6frf9oxqqcf3o8wbog5tx9t4oy5tzityfn6qc5q3bdmg5qrwxsrewuz9fruegz1oexwgtlcsicp5e7bzqaqzeq1llpv4svs
# zip
# [ união entre índices // chaves // chaves_valores de iteráveis ] [ objeto de memória ] [ gerador de tupla ]
# [ 2 args mínimo ] [ equivalência numérica entre dados de iteráveis ] [ não equivalência gera ignoração de dados ]
# [ isento de erro ] [ zip em comprehension ]

# Sintaxe: [ zip(iterável, iterável...) ]
"======================================================================================================================"
conj = {'1º dado', '2º dado'}
dicio = {'3º dado': None, '4º dado': None}
lista = ['5º dado', '6º dado']
tupla = ('7º dado', '8º dado')
zipagem = zip(lista, tupla, conj, dicio.items())

print(tuple(zipagem))
# (('5º dado', '7º dado', '1º dado', ('3º dado', None)), ('6º dado', '8º dado', '2º dado', ('4º dado', None)))

lista = ['nome']
tupla = 'Lucas', 'Farias'
zipagem2 = zip(lista, tupla)
print(tuple(zipagem2))  # (('nome', 'Lucas'),) [ dado excedente ignorado ]: 'Farias'

string = 'abcdefghijklmnopqrstuvwxyz'
lista2 = list(range(1, 27))
zipagem3 = zip(string, lista2)
print(tuple(zipagem3))
# (('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6), ('g', 7), ('h', 8), ('i', 9), ('j', 10), ('k', 11),
# ('l', 12), ('m', 13), ('n', 14), ('o', 15), ('p', 16), ('q', 17), ('r', 18), ('s', 19), ('t', 20), ('u', 21),
# ('v', 22), ('w', 23), ('x', 24), ('y', 25), ('z', 26))

tupla2 = ('dia',) * 31
conj2 = set(range(1, 32))
zipagem4 = zip(tupla2, conj2)
print(tuple(zipagem4))
# (('dia', 1), ('dia', 2), ('dia', 3), ('dia', 4), ('dia', 5), ('dia', 6), ('dia', 7), ('dia', 8), ('dia', 9),
# ('dia', 10), ('dia', 11), ('dia', 12), ('dia', 13), ('dia', 14), ('dia', 15), ('dia', 16), ('dia', 17), ('dia', 18),
# ('dia', 19), ('dia', 20), ('dia', 21), ('dia', 22), ('dia', 23), ('dia', 24), ('dia', 25), ('dia', 26), ('dia', 27),
# ('dia', 28), ('dia', 29), ('dia', 30), ('dia', 31))

lista3 = ['dia'] * 10
tupla3 = tuple(range(1, 11))
zipagem4 = zip(lista3, tupla3, ['de janeiro'] * 10)
print(tuple(zipagem4))
# (('dia', 1, 'de janeiro'), ('dia', 2, 'de janeiro'), ('dia', 3, 'de janeiro'), ('dia', 4, 'de janeiro'),
# ('dia', 5, 'de janeiro'), ('dia', 6, 'de janeiro'), ('dia', 7, 'de janeiro'), ('dia', 8, 'de janeiro'),
# ('dia', 9, 'de janeiro'), ('dia', 10, 'de janeiro'))

alunos = ['Lucas', 'Juvêncio', 'Alfredo']
notas = [7.4, 8.1, 6.6]
notas2 = [8.5, 8.6, 7.9]

# Zip em comprehension
set_comprehension = {(dados[0] + dados[1]) / 2 for dados in zip(notas, notas2)}
print(set_comprehension)   # {7.95, 8.35, 7.25}

dict_comprehension = {dados[0]: dados[1] for dados in zip(alunos, set_comprehension)}
print(dict_comprehension)  # {'Lucas': 7.95, 'Juvêncio': 8.35, 'Alfredo': 7.25}

list_comprehension = [(dados[0] + dados[1]) / 2 for dados in zip(notas, notas2)]
print(list_comprehension)  # [7.95, 8.35, 7.25]

generator = ((dados[0] + dados[1]) / 2 for dados in zip(notas, notas2))
print(tuple(generator))    # (7.95, 8.35, 7.25)
"======================================================================================================================"
