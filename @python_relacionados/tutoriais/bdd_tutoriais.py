

# rrip1haxywzwvze9kcaqgeyz8535ykqdwnuh8wedj3peomjlhe2suiiootphggd1hygby6adam3semgoyac78r5mq3c3jde9ct2k
# Coleção dicionário: acesso de dados pela chave matriz vs acesso de dados pela chave aninhada
"======================================================================================================================"
dicio = {'dados do país': {'nome': 'Brasil', 'língua': 'português', 'estados': 27, 'clima': 'tropical'}}

"Quem é a chave matriz desse dicionário?"
print(dicio['dados do país'])  # {'nome': 'Brasil', 'língua': 'português', 'estados': 27, 'clima': 'tropical'}

"Quem são as chaves aninhadas desse dicionário?"
print(dicio['dados do país']['nome'])
print(dicio['dados do país']['língua'])
print(dicio['dados do país']['estados'])
print(dicio['dados do país']['clima'])
"======================================================================================================================"



# kavj4n3dbawxmm26unsxhj7mgig66hge34uurmc2a8t7ilijxdukbzez2p1941wb3bjamyh8pkfcnr8o67lsvecwmgpj23pncffd
# Combinação de key=lambda com max & min para ampliar critério de filtragem
# [ filtragem de dados textuais / numéricos ] Sintaxe: min/max(var iterável, chave lambda var integrada, ação lambda)
"======================================================================================================================"
contexto = ('print', 'valor da variável', 'variável própria', 'variável nova')
from random import randint

lista = [
    {'nome': 'Lucas', 'idade': 27},
    {'nome': 'Farias', 'idade': 14},
    {'nome': 'Santos', 'idade': 39},
    {'nome': 'Sousa', 'idade': 71}]

print(max(lista, key=lambda cada_valor: cada_valor['idade']))  # {'nome': 'Sousa', 'idade': 71}
print(min(lista, key=lambda cada_dado: cada_dado['nome']))     # {'nome': 'Farias', 'idade': 14}

lista_de_velocidades = [
    {'velocidade': randint(1, 200)},
    {'velocidade': randint(1, 200)},
    {'velocidade': randint(1, 200)}]

maior_velocidade = max(lista_de_velocidades, key=lambda cada_velocidade: cada_velocidade['velocidade'])
print(maior_velocidade)  # {'velocidade': 125}

lista2 = [
    {'nome': 'Chop Suey', 'nº de reproduções': 27},
    {'nome': 'Spiders', 'nº de reproduções': 14},
    {'nome': 'Toxicity', 'nº de reproduções': 39},
    {'nome': 'Vermilion pt2', 'nº de reproduções': 71}]

mais_tocada = max(lista2, key=lambda cada_faixa: cada_faixa['nº de reproduções'])['nome']
print(mais_tocada)  # Vermilion pt2
"======================================================================================================================"



# pbt2mh9o8lvu5u62f8rzjcsypsb27pf6fdzqi2y33kcw3clnf3tkx5m7mf9xkd3u1kjnyogq8nmu574l66utjf4m1ibfp6fe3vyz
# Comprehension: exemplo com dois loops for internos (avançado)
# [ união entre coleções (listas) por concatenação em tupla ]
"======================================================================================================================"
from random import shuffle
naipes = ['♥', '♦', '♣', '♠']
cartas = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
baralho = []
jogador1 = []
jogador2 = []
jogador3 = []
jogador4 = []
cartas_por_jogador = 9
contar = 0


def criar_baralho(sorteio_ordem: bool = False) -> list:
    global baralho

    if sorteio_ordem is True:
        baralho = [(cada_carta + cada_naipe) for cada_naipe in naipes for cada_carta in cartas]  # exemplo aqui
        shuffle(baralho)
    return baralho


def distribuir_cartas(jogadores: int):
    global baralho, contar, cartas_por_jogador, jogador1, jogador2, jogador3, jogador4

    if jogadores < 2 or jogadores > 4:
        print('Número de jogadores não permitido (mínimo: 2, máximo: 4)')

    elif jogadores == 4:
        cartas_por_jogador = jogadores * cartas_por_jogador
        contar = cartas_por_jogador
        while contar > 0:
            jogador1.append(baralho.pop()), jogador2.append(baralho.pop()),\
            jogador3.append(baralho.pop()), jogador4.append(baralho.pop())
            contar -= 4

    elif jogadores == 3:
        cartas_por_jogador = jogadores * cartas_por_jogador
        contar = cartas_por_jogador
        while contar > 0:
            jogador1.append(baralho.pop()), jogador2.append(baralho.pop()), jogador3.append(baralho.pop())
            contar -= 3

    elif jogadores == 2:
        cartas_por_jogador = jogadores * cartas_por_jogador
        contar = cartas_por_jogador
        while contar > 0:
            jogador1.append(baralho.pop()), jogador2.append(baralho.pop())
            contar -= 2

if __name__ in '__main__':
    print(criar_baralho(True))
    distribuir_cartas(2)
"======================================================================================================================"

# lyndhav9kgsc91p4iiw7iaspr5bs8snmysonqd4fb4ghf686ut63g1dyn5379yrixe1otdymzy7d9htit73vsjnim5j2vsjvjax2
# Concatenação para classes lista e string
# [ exclusivo lista/string ] [ operador aritmético de adição tipo 1 & 2 ] [ mesclador de dados iteráveis ]
"======================================================================================================================"
contexto = ('print', 'valor da variável', 'variável própria', 'nova variável')
contexto2 = ('pós-variável',)

"Exemplo de mesclagem de 2 listas (lista literal + lista em variável)"
#############################################
lista = ['vs', 'Brasil']
lista2 = ['Alemanha'] + lista
print(lista2)  # ['Alemanha', 'vs', 'Brasil']
#############################################

"Exemplo de mesclagem de 2 strings (string em variável + string literal)"
###############################
string = '...'
print(string + '___')  # ...___
###############################

"Exemplo de mesclagem de 2 listas (uso do tipo 2 de concatenação) (pós-variável) (+=)"
#########################################################################
lista_string = lista2 + string.split()
lista_string += '___'
print(lista_string)  # ['Alemanha', 'vs', 'Brasil', '...', '_', '_', '_']
#########################################################################
"======================================================================================================================"



# c2wem8r5jyyc6t5nnn8plcovbybgs2aaz3ldll32bb5sh2w7rtuyg4uby9fnys4l12i66esraq5mk5hzu3givji94ml8nu1euayj
# Cores ansi sinxtaxe para uso em algoritmo
"======================================================================================================================"
"Qual é a regra?"
# Usar o sintaxe: \033[m
"Como funciona?"
# Há de 1 a 3 argumentos que podem ser passados, sendo o 1º e 2º, mandatórios
"Onde ficam os argumentos na sintaxe?"
# Entre o [ e m
"Alguma observação?"
# Sim, o texto a ser colorido precisa estar dentro da string da sintaxe , e após o "m"

"Exemplos com 1º argumento"
sem_arg = '\033[0:30mtexto normal'
arg1 = '\033[1:30mtexto em negrito'
arg4 = '\033[4:30mtexto sublinhado'
arg7 = '\033[7:30mtexto com plano de fundo'

print(sem_arg, '\n', arg1, '\n', arg4, '\n', arg7)

"Exemplos com 2º argumento"
arg30 = '\033[0:30mcor'
arg31 = '\033[0:31mcor'
arg32 = '\033[0:32mcor'
arg33 = '\033[0:33mcor'
arg34 = '\033[0:34mcor'
arg35 = '\033[0:35mcor'
arg36 = '\033[0:36mcor'
arg37 = '\033[0:37mcor'

print(arg30, arg32, arg33, arg34, arg35, arg36, arg37)

"Exemplo com 3º argumento [ não mandatório ]"
arg40 = '\033[0:37:40mfundo'
arg41 = '\033[0:36:41mfundo'
arg42 = '\033[0:35:42mfundo'
arg43 = '\033[0:34:43mfundo'
arg44 = '\033[0:33:44mfundo'
arg45 = '\033[0:32:45mfundo'
arg46 = '\033[0:31:46mfundo'
arg47 = '\033[0:30:47mfundo'

print(arg40, '\n', arg41, '\n',  arg42, '\n',  arg43, '\n',  arg44, '\n',  arg45, '\n',  arg46, '\n',  arg47)

"Planos de fundo vazios [ 3 args mandatórios ]"
print('\033[7:30:40m_____\033[m')  # Exemplo de fundo com texto escondido para controlar o tamanho fo plano de fundo
print('\033[7:31:41m')
print('\033[7:32:42m')
print('\033[7:33:43m')
print('\033[7:34:44m')
print('\033[7:35:45m')
print('\033[7:36:46m')
print('\033[7:37:47m')
"======================================================================================================================"



# taayvapm6shoofn7ymfdxvxk11rysaack8xbutmhvf4eghwb5l54zgzp5jhionfoewqnafn3oqc84pukc99ovc7v7x6tbexozvd4
# Counter regular vs counter most common tupla
"======================================================================================================================"
from sys import getsizeof as size
from collections import Counter

var = """
Am 9. November 1989 sitzt Günter Schabowski, Mitglied des Politbüros der Deutschen Demokratischen Republik (DDR),
auf einem roten Sessel im Pressezentrum des Zentralkomitees der Staatspartei SED in Ostberlin. Eine Stunde lang
antwortet er auf Fragen von Journalisten aus der ganzen Welt. Kurz vor dem Ende hat ein italienischer Journalist noch
eine Frage. Schabows­ki nimmt einen Zettel aus der Jacke. Nur kurz hat er den Text davor gelesen, eigentlich soll er
die Medien erst am nächsten Morgen darüber informieren. Es soll in Zukunft einfacher werden, aus der DDR auszureisen,
sagt er. Das ist bis jetzt nämlich noch verboten. Deshalb sind viele Tausend DDR-Bürger zuletzt über die damalige
Tschechoslowakei in die Bundes­republik Deutschland geflohen. Sie wollen sich nicht mehr in ihrem Land einsperren
lassen. Außerdem wollen sie politische Reformen. Die Regierung muss deshalb etwas tun. Jetzt sollen DDR-Bürger Reisen
beantragen können. Die Anträge sollen schnell geprüft werden. Es ist 18.53 Uhr, als Schabowski den Zettel nimmt und
die Sätze vorliest. Im Fernsehen der DDR ist die Pressekonferenz live zu sehen. Ein Journalist will wissen, ab wann
die neue Regelung gelten soll. Schabowski zuckt mit den Schultern. Dann sagt er die Worte, nach denen die Welt eine
andere ist: „Das tritt nach meiner Kenntnis … ist das sofort, unverzüglich.“ Ein Fehler. Erst ab dem nächsten Morgen,
vier Uhr, sollte die Regel eigentlich gelten. An der Grenze ist noch niemand informiert.
"""

"Counter gera uma grande quantidade de armazenamento"
"Sua vantagem é somente o acesso fácil ao dado por chave"
scan = Counter(var.split())
print(size(scan))   # 5184
print(scan)

"Counter com most common tupla gera quantidade de armazenamento bem reduzida"
"O acesso não é fácil, e por isso, além de fazer o procedimento, é preciso gerar uma pequeno algoritmo"
scan2 = Counter(var.split()).most_common(len(var.split()))  # tuple() pode ser usado para diminuir ainda mais
print(size(scan2))  # 724
print(scan2)

"Esse pequeno algoritmo consegue achar o dado desejado"
data = input('Data name -> ')
for each_data in scan2:
    if each_data[0] == data:
        print((each_data[0], each_data[1]))
"======================================================================================================================"



# mewnhkwji3m7nym29en2ojahbywj1ryhzp9rgw316x6b5sabcp5q8zj58r961xzmvxcytm5gxcutd7hbd2eglnecjotbv8vs9gnd
# Criação de loop customizado usando [ iter() ] + [ next() ]
"======================================================================================================================"


def itera(iterable):
    var = iter(iterable)
    while True:
        try:
            print(next(var), end=' ')  # v a i   t o m a r   n o   c o o l
        except StopIteration:
            break

itera('vai tomar no cool')
print('\n')

frase = iter('vai tomar no cool')
while True:
    try:
        print(next(frase), end=' ')  # v a i   t o m a r   n o   c o o l
    except StopIteration:
        break
"======================================================================================================================"



# kh28ccomhl9l7bb1hefrn98tyk921vbn6h1nx4v1mofbh7u9vbsqyizpire6i7nkwurfeoc2z8bp83ubqwd8pjyktzavnpffxdg3
# Criação de pastas aninhadas sem precisar entrar na pasta matriz
"======================================================================================================================"
from os import chdir, mkdir, makedirs
chdir('C:\\Users\\Lucas\\Desktop')

"OBS: para criar pastas dentro da pasta aninhada, 1º cria-se a pasta aninhada"
"OBS: depois acesse-a, repetindo o mesmo caminho, só que dessa vez inserindo [ /novo nome de pasta ]"

# Forma menos eficiente
mkdir('1')
mkdir('1/2')    # Isso é entendido como acessar a 1ª pasta e criar nela, uma 2ª pasta
mkdir('1/2/3')  # =============================== 1ª e 2ª pasta, e criar nela, uma 3ª pasta

# Forma mais eficiente
makedirs('Lucas/Farias/Santos')  # Realiza o mesmo procedimento, porém em 1 linha
"======================================================================================================================"



# yty51l1btu91uq2zb4enmqhsrkxj9ulds86ovbp3b8s8vq4ge3y8rcfv9wj9n6fcuca3u55klpmuupl44dn7en7fyn6sc5o5bo1h
# Dict comprehension: diferentes tipos de iteração
"======================================================================================================================"
modelo = {1: True, 2: 'False', 3: round(7.7)}

# Dict comprehension genérico
dicio = {cada_dado: cada_dado for cada_dado in modelo}

# Dict comprehension: chaves clonadas como valores
dicio3 = {dados: dados for dados in modelo}
print(dicio3)             # {1: 1, 2: 2, 3: 3}

# Criação de dicionário com valores que são clonadas como valores
dicio4 = {dados: dados for dados in {1: True, 2: 'False', 3: round(7.7)}.values()}
print(dicio4)             # {True: True, 'False': 'False', 8: 8}

# Criação de dicionário com chaves & valores como chave & valor
dicio_chave_valor = {dados: dados for dados in {1: True, 2: 'False', 3: round(7.7)}.items()}
print(dicio_chave_valor)  # {(1, True): (1, True), (2, 'False'): (2, 'False'), (3, 8): (3, 8)}

modelo = {1: True, 2: 'False', 3: round(7.7)}

"DICT COMPREHENSION GENÉRICO (CLONADOR DE CHAVES)"
# {1: 1, 2: 2, 3: 3}
dicio = {cada_dado: cada_dado for cada_dado in modelo.keys()}  # pode ser feita sem o método .keys()
print(dicio)

"DICT COMPREHENSION COM VALOR COMO CHAVE E VALOR"
# {True: True, 'False': 'False', 8: 8}
dicio2 = {cada_dado: cada_dado for cada_dado in modelo.values()}
print(dicio2)

"DICT COMPREHENSION TUPLA CHAVE VALOR: CHAVE VALOR"
# {(1, True): (1, True), (2, 'False'): (2, 'False'), (3, 8): (3, 8)}
dicio_chave_valor = {dados: dados for dados in modelo.items()}
print(dicio_chave_valor)

"PODE-SE COMBINAR DICT COMPREHENSION COM RANGE, CONTANTO QUE TRÊS CONDIÇÕES SEJAM CUMPRIDAS"
"1. EQUIVALÊNCIA DE DADOS (MESMA QUANTIDADE DE ÌNDICES)"
"2. COMPATIBILIDADE DE COLEÇÕES (CONJUNTO É UM EXEMPLO DE COLEÇÃO NÃO COMPATÍVEL)"
"3. RANGE PRECISA RECEBER O RANGE COM O MÉTODO len(DO NOME DA VAR QUE SERÁ A CHAVE DO DICT COMPREHENSION)"

# {1: True, 2: 'False', 3: 8}
lista = [1, 2, 3]
tupla = (True, 'False', round(7.7))  #           range(0, 3)
dicio = {lista[dados]: tupla[dados] for dados in range(len(lista))}
print(dicio)

# {True: 1, False: 2, 8: 3}
lista2 = [1, 2, 3]
lista3 = [True, False, round(7.7)]
dicio2 = {lista3[dados]: lista2[dados] for dados in range(len(lista3))}
print(dicio2)

# {True: 1, False: 2, 8: 3}
tupla2 = (1, 2, 3)
tupla3 = (True, False, round(7.7))
dicio3 = {tupla3[dados]: tupla2[dados] for dados in range(len(tupla3))}
print(dicio3)

# {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
range_ = range(0, 8)
string = 'abcdefgh'
dicio4 = {string[cada_dado]: range_[cada_dado] for cada_dado in range(len(string))}
print(dicio4)

"COLEÇÃO CONJUNTO NÃO PODE SER INFLUENCIADA POR DICT COMPREHENSION"  # TypeError: 'set' object is not subscriptable
# conj = {1, 2, 3}
# conj2 = {True, False, round(7.7)}
# dicio = {conj2[dados]: conj[dados] for dados in range(len(conj2))}
# print(dicio)
"======================================================================================================================"



# rrd9xktzdx8uu3o7cimhd3hd2v63xxnsqbuy6119q9yhbd6az4g6qec8p4eocu6r7tgai9hkrwsfrieyrv9chhmovwyynhay38gs
# Dict comprehension: uso de condição if sem else
"======================================================================================================================"
tipo = 'ímpar'
lista_numeros = list(range(1, 8))
dicio = {dados: tipo for dados in lista_numeros if dados % 2}
print(dicio)  # {1: 'ímpar', 3: 'ímpar', 5: 'ímpar', 7: 'ímpar'}
"======================================================================================================================"



# mm24czilv3nasuvxx973447npib97jt5ymj7a4uqf3wyqwwch5tjhzkgy22oqycqagb4y5wn1hqlm7ypqgbo5gb4kjqq1slpl44f
# Dict comprehension: uso de condição if & else, ação em parênteses para organização ou geração de tupla
"======================================================================================================================"
tipos = 'par ímpar'
lista_numeros = list(range(1, 8))
dicio = {dados: (tipos[0:3] if not dados % 2 else tipos[4:]) for dados in lista_numeros}  # parênteses ilustrativo
print(dicio)  # {1: 'ímpar', 2: 'par', 3: 'ímpar', 4: 'par', 5: 'ímpar', 6: 'par', 7: 'ímpar'}
"======================================================================================================================"



# r3wje5qq63qdc9vthhg1ezd4xc2675fxypob8u6t5272v2ajm218wcuuj59nv8r2joateyj5hjq6pnaa29wj3haj88otd2slb5u8
# Diferenças de comportamento de max & min para tipos de dados numéricos & string
"======================================================================================================================"
contexto = ('print', 'valor da variável', 'variável própria', 'variável nova')

########################################################
"Selação [ min() ] em string, priorização de cacha alta"
lista = min(['lista', 'range', 'tupla', 'conjunto', 'dicionário', 'String'])
print(lista)  # String
########################################################

############################################
"Seleção [ min() ] em string, seleção nomal"
lista2 = min(['lista', 'range', 'tupla', 'conjunto', 'dicionário', 'string'])
print(lista2)  # conjunto
############################################

###############################################################
"Seleção [ max() ] em string, não há priorização de cacha alta"
lista3 = max(['lista', 'Range', 'tupla', 'conjunto', 'dicionário', 'String'])
print(lista3)  # tupla
###############################################################

############################################
"Seleção [ max() ] em string, seleção nomal"
lista4 = max(['lista', 'range', 'tupla', 'conjunto', 'dicionário', 'string'])
print(lista4)  # tupla
############################################

###################################################
"Seleção [ max() ] & [ min() ] com string numérica"
string = '2892458'
print(min(string))  # 2
print(max(string))  # 9
###################################################

###################################################
"Seleção [ max() ] & [ min() ] com classe numérica"
conj = {1, 22.7, 33, 15, 9.9}
print(min(conj))    # 1

conj2 = max(conj.copy())
print(conj2)        # 33
###################################################
"======================================================================================================================"



# i2he7doebnf649e4ajxipph3swbqmx8dbuvnroophv7awde9z42gpmjt82gho235mwxjjqknvwsszlgn14z5i94nz46bi1xw9k98
# Diferenças entre namedtuple vs tupla
# [ tupla é mais simples de criar ]  [ tupla nomeada não é tão simples, e requer duas variáveis ]
# [ tupla é mais fácil de entender ] [ tupla nomeada requer mais experiência ]
# [ tupla é menos semântica em casos de índices aninhados ]        [ índexação     ]
# [ tupla nomeada é mais semântica em casas de índices aninhados ] [ notação ponto ]
"======================================================================================================================"
from collections import namedtuple

tupla = (('nome', 'Lucas'), ('idade', 27), ('esporte', 'ciclismo'))
tupla_nomeada = namedtuple('título', ['nome', 'idade', 'esporte'])
pessoa = tupla_nomeada(nome='Lucas', idade=27, esporte='ciclismo')

print(tupla)           # (('nome', 'Lucas'), ('idade', 27), ('esporte', 'ciclismo'))
print(tupla_nomeada)   # <class '__main__.título'>
print(pessoa)          # título(nome='Lucas', idade=27, esporte='ciclismo')

print(tupla[2][1])     # ciclismo [ mais complexo ]
print(pessoa.esporte)  # ciclismo [ mais semântico ]
"======================================================================================================================"



# sh95ht1jmblynsqjgzpns69d5ae6zqf1c87xx1mbnlq4icp24fj186yqdxsjfpj3jj6uvuv2eoyxzn1ev4qm7jox79ld4mpo6n6m
# Emulação de conjunto através de Counter() [ conjunto = desorganizado ] [ Counter = organizado ]
"======================================================================================================================"
from collections import Counter

string = """
Python é uma linguagem de programação de alto nível,[4] interpretada, de script, imperativa, orientada a objetos,
funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.[1] Atualmente possui um modelo de 
desenvolvimento comunitário, aberto e gerenciado pela organização sem fins lucrativos Python Software Foundation.
"""
print(tuple(Counter(string.split()).keys()))
# ('Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'alto', 'nível,[4]', 'interpretada,', 'script,',
# 'imperativa,', 'orientada', 'a', 'objetos,', 'funcional,', 'tipagem', 'dinâmica', 'e', 'forte.', 'Foi', 'lançada',
# 'por', 'Guido', 'van', 'Rossum', 'em', '1991.[1]', 'Atualmente', 'possui', 'um', 'modelo', 'desenvolvimento',
# 'comunitário,', 'aberto', 'gerenciado', 'pela', 'organização', 'sem', 'fins', 'lucrativos', 'Software', 'Foundation.')

print(set(string.split()))
# {'tipagem', 'orientada', 'alto', 'Rossum', 'funcional,', 'Guido', 'de', 'objetos,', 'forte.', 'lucrativos',
# '1991.[1]', 'sem', 'a', 'modelo', 'é', 'por', 'uma', 'lançada', 'Atualmente', 'comunitário,', 'pela', 'dinâmica',
# 'organização', 'possui', 'interpretada,', 'um', 'linguagem', 'fins', 'Foi', 'script,', 'e', 'imperativa,', 'Software',
# 'nível,[4]', 'Python', 'em', 'aberto', 'Foundation.', 'desenvolvimento', 'gerenciado', 'van', 'programação'}
"======================================================================================================================"



# 4xjjo995wcen9rsg8elfyrbzq4giu82l1oj48cr4ff4lhtqi8v8quow8hni1doau9nl8xkejkvuzgazxzvd4mey7vbdtbb22zg28
# Esquivamento de erro [ FileExistsError ]
"======================================================================================================================"
from os import chdir, mkdir, makedirs

xjjo9_obs = 'impedimento do erro FileExistsError funciona somente com o método makedirs()'

chdir('c:\\users\\lucas\\desktop')

mkdir('ok')

makedirs('ok', exist_ok=True)  # O segundo argumento impede o erro = FileExistsError
"======================================================================================================================"



# ubdtb9w7ekxbhfaout9ruspv6jk7wxuwtlfhvhp3xgmdoax88equc97sd2tbh7na31tumvdkmkgk1pmkhvkxri2wmqz6f162dxhu
# Exclusão de caractere string dentro de iteráveis
"======================================================================================================================"
"O procedimento por etapas separadas"
lista_string = ' '.join(lista)
print(lista_string)             # Lucas Farias Santos de Sousa
string_lista_separador = lista_string.split('a')
print(string_lista_separador)   # ['Luc', 's F', 'ri', 's S', 'ntos de Sous', '']
lista_string_final = ' '.join(string_lista_separador)
print(lista_string_final)       # Luc s F ri s S ntos de Sous

lista = ['Lucas', 'Farias', 'Santos', 'de', 'Sousa']
lista2 = ' '.join(' '.join(lista).split('a'))
print(lista2)   # Luc s F ri s S ntos de Sous

string = 'Lucas Farias Santos de Sousa'
string2 = ' '.join(string.split('a'))
print(string2)  # Luc s F ri s S ntos de Sous

tupla = 'Lucas', 'Farias', 'Santos', 'de', 'Sousa'
tupla2 = ' '.join(' '.join(tupla).split('a'))
print(tupla2)   # Luc s F ri s S ntos de Sous
"======================================================================================================================"



# zc8g8o4ocpglb6lwmwlg792fx6zbv85f32lzxm228z3ckmxjx4nm8z7z5g9df7oijt935cemdy55kg6vt1mciw2jh7tcbkabng6i
# Tratamento de erro de texto sem bloquear em caso de dado indesejado [ relativamente eficiente ]
# [ bloquear em caso de dado indesejado mais eficiente ]
"======================================================================================================================"
from error_handling import string_incompatible_data

nome = input('Seu nome -> ')

for each_data in nome:
    if each_data in string_incompatible_data:
        nome = ' '.join(tuple(filter(lambda var: not var == each_data, nome)))
        nome = nome.split()
        nome = ' '.join(nome)
        nome = nome.title()
print(nome)
"======================================================================================================================"



# 38m4yvw7lg45oqlikkikxta7h2tmvjuhw8mp8njld2cqsalsxb2ktwojn9jwcff2xxjk1xyugtc1atsxqqlidfipngg4nkkopzek
# Função: função de maior grandeza [ High order function ] [ HOF ]
"======================================================================================================================"


def soma(p1, p2):
    return p1 + p2


def diminuir(p1, p2):
    return p1 - p2


def var(f, p1, p2):
    return f(p1, p2)         # print(f(p1, p2)

print(var(diminuir, 17, 7))  # var(diminuir, 17, 7) [ resultado = 10 ]
"======================================================================================================================"



# xak5vv1gamyli4t3uqlgu2y79nfgfmuimpv7vitort7jk17npbf4q9z8prvoc97urf7sbrphop5to2iaq728u28tkxk4pl75xv6g
# Função: funções aninhadas e suas formas de retorno [ inner functions ] [ nested functions ]
"======================================================================================================================"
def pais(var_pais):
    def caracteristicas():
        from random import choice
        return choice([' é frio', ' é tropical', ' é lotado', ' não neva', ' é festivo'])
    return var_pais + caracteristicas()

print(pais('Alemanha'))
print(pais('Brasil'))
print(pais('Bélgica'))

# Alemanha é festivo
# Brasil é frio
# Bélgica é lotado


def nome(meu_nome):
    def banco_de_dados():
        from random import choice
        sobrenomes = ['Farias', 'Almeida', 'Costa', 'Fernandez', 'Brigadeiro', 'Filho', 'Augusto']
        return 'Meu nome é {} e meu sobrenome é {}'.format(meu_nome, choice(sobrenomes))
    return banco_de_dados()
print(nome('Lucas'))  # Meu nome é Lucas e meu sobrenome é Fernandez
"======================================================================================================================"



# 34l6tgh4lqa55zlyrqgd4s44vlz4lgq88ejm22ykqo134yql4w7hpc3rzhzb1shk4fnfzb2nkmqpxcpf95icbun7ippj2rhua7u6
# Gerador: dependência de casting vs independência de casting [ dependência de next() ]
"======================================================================================================================"
gerador = tuple((each_data for each_data in 'Lucas Farias'))
print(gerador[0])      # L     O índice específico só é acessível no gerador, por causa do [ casting ]
print(gerador[1])      # u     O índice específico só é acessível no gerador, por causa do [ casting ]

gerador_ = (each_data for each_data in 'Lucas Farias')
print(gerador_[0])     # TypeError: 'generator' object is not subscriptable
print(next(gerador_))  # L     O índice específico é acessível por next(), sem depender de [ casting ]
print(next(gerador_))  # u     O índice específico é acessível por next(), sem depender de [ casting ]
"======================================================================================================================"



# 3jm4me1dimvovx6lka3i3np5s58as37s23uopu44vgq8buz22ctqi1k8tdx5ggumwbe6nw6avkkruz8pm1qyw8v6drcvwv9hu2ep
# Gerando senhas fortes
"======================================================================================================================"
from passlib.hash import pbkdf2_sha256 as crypto
name = crypto.hash('', rounds=200_000, salt_size=16)
print(name)

# $pbkdf2-sha256$200000$oxSilPKecy6F8F7r/R/DGA$y745O86eHu/2sXHotJO4oXC.uB21vwlbkph7S1eLf3Q
# $pbkdf2-sha256$200000$1trb.z.HMIZQyrn3/v9fyw$LMLpUoTd./XuTNTLcooioU50qgeVtAYtGRe9mMLNiMg
"======================================================================================================================"



# stbh8tksz1h8qg8ac2w64agq5u88fkac3c5q26z9w8iz2lp6os4srx6lhwg96igen49otc3trfu1ugu9b3dpjf7gw4iw1hkusayq
# Interação entre casting & método após conversão do dado para outra classe
"======================================================================================================================"
inteiro = 2892458
print(str(inteiro).replace('8', '{}'))                                                                 # 2{}9245{}
inteiro2 = 2892458
print(str(inteiro2).replace('8', '').replace('2', '').replace('9', ''))                                       # 45
inteiro3 = str(7294185).replace('8', '').replace('2', '').replace('7', '').replace('9', '').replace('1', '')  # 45
print(inteiro3)

# [ .replace() ] deve estar [ fora & após ] a [ conversão cast ]
"======================================================================================================================"



# dzlqumzqstj18en4eqb9vornw5tfdx5efokq4m3uwrfrvr4m12z9l53kszy6lx1urqg9evxm6a7ebm7vacht4e1g9sm35o5h35op
# Iteração alternativa com dados iteráveis & não iteráveis com loop while [ iteração principal  = loop for ]
"======================================================================================================================"
lista = ['Lucas', 'Farias', 'Santos', 'de', 'Sousa']
indice = 0
while indice < len(lista):  # [ iteração com classe iterável ] [ lista ]
    print(lista[indice])
    indice += 1
    # Lucas
    # Farias
    # Santos
    # de
    # Sousa

indice = 0
range_ = range(1, 11)
while indice < len(range_):
    print('dia {}'.format(range_[indice]), end='  ')
    indice += 1
# dia 1  dia 2  dia 3  dia 4  dia 5  dia 6  dia 7  dia 8  dia 9  dia 10
"======================================================================================================================"



# o99ko1exdg8lvqqpjq7p2xxn6as65cmc2z8sh2adwlagwpfmqgy25qwbyyxf8ii2nqngkgrxy5aoaggn3t8a5vguclkq6ltdnacs
# Diferentes tipos de iteração [ loop for = delimitador de bloco ] & [ comprehension = em linha ]
"======================================================================================================================"
conj = {False, 1j, 'python', 81 ** 0.5}
dicio = {'python': 'string', 1j: 'complexo', False: 'booleano', 81 ** 0.5: 'inteiro'}
lista = [False, 1j, 'python', 81 ** 0.5]
tupla = tuple(range(1, 11))

"Iteração em [ variável ] de [ classe conjunto em variável ] usando [ comprehension ]"
##########################################
conj2 = {dados for dados in conj}
print(conj2)  # {False, 9.0, 1j, 'python'}
##########################################

"Iteração em [ print ] de [ classe conjunto literal ] usando [ comprehension ]"
##########################################################################################
print({dados for dados in {False, 1j, 'python', 81 ** 0.5}})  # {False, 9.0, 1j, 'python'}
##########################################################################################

"Iteração de [ classe dicionário em variável ] usando [ loop for ]"
#######################################################################################################
for dados in dicio.items():
    print(dados, end=' ')  # ('python', 'string') (1j, 'complexo') (False, 'booleano') (9.0, 'inteiro')
#######################################################################################################

"Iteração em [ print ] de [ classe dicionário literal ] usando [ comprehension ]"
######################################################################################################################
print(tuple(dados for dados in {'python': 'string', 1j: 'complexo', False: 'booleano', 81 ** 0.5: 'inteiro'}.items()))
# (('python', 'string'), (1j, 'complexo'), (False, 'booleano'), (9.0, 'inteiro'))
######################################################################################################################

"Iteração com de [ classe lista em variável ] usando [ loop for ]"
################################################
for dados in lista:
    print(dados, end=' ')  # False 1j python 9.0
################################################

"Iteração em [ print ] de [ classe lista literal ] usando [ comprehension ]"
##########################################################################################
print([dados for dados in [False, 1j, 'python', 81 ** 0.5]])  # [False, 1j, 'python', 9.0]
##########################################################################################

"Iteração de [ classe tupla em variável ] usando [ loop for ]"
#################################################
for dados in tupla:
    print(dados, end=' ')  # 1 2 3 4 5 6 7 8 9 10
#################################################

"Iteração de [ classe tupla literal ] usando [ comprehension ]"
#########################################################################################
print(tuple((dados for dados in tuple(range(1, 11)))))  # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#########################################################################################
"======================================================================================================================"



# dlgbbfiiffalmqdhmsmuh4a88hgzzz3c832xczlbrr3n7gvzje7w83xlexpnknjolaplt73rhvy31om5fpjdy9r1sl1qm6fdc61o
# List comprehension: uso de condição if sem else
"======================================================================================================================"
tipo = 'ímpar'
dados_num = list(range(1, 8))
resultado = ['{} ímpar'.format(dados) for dados in dados_num if dados % 2]
print(resultado)  # ['1 ímpar', '3 ímpar', '5 ímpar', '7 ímpar']
"======================================================================================================================"



# zxk4a1283sm7yizvsewpdch93xh8t89u5qerc7v5f8cyxv7zaumjk999u2i6vn5mudsh6twr1185mepfdlovs89io4u3mhvnoksc
"======================================================================================================================"
from random import shuffle

zxk4a_titulo = 'List comprehension - Diferença do list comprehension com if vs if e else'

tipos = 'par ímpar'

valores = list(range(1, 8))

shuffle(valores)

resultado_com_if = [cada_num for cada_num in valores if cada_num % 2]
# Quando if está sozinho, ele fica após o loop

resultado_com_if_else = [tipos[0:3] if not cada_num % 2 else tipos[4:] for cada_num in valores]
# Quando há if e else, eles ficam antes do loop

print(resultado_com_if)       # [1, 3, 5, 7]
print(resultado_com_if_else)  # ['par', 'ímpar', 'ímpar', 'par', 'ímpar', 'par', 'ímpar']
"======================================================================================================================"



# g4d1u8nmuumqdl8w6dy3rua5au2ayxf9fbmrv9ghj327xgk5nnyv71lct9n7shtf8h494hyouzxdj8kahy5de5c7oowj36x99u1l
# Loop for: agrupamento de dados em forma de cascata
"======================================================================================================================"
nome = 'Lucas '
for seq in range(1, 8):
    print(seq * nome)

# Lucas
# Lucas Lucas
# Lucas Lucas Lucas
# Lucas Lucas Lucas Lucas
# Lucas Lucas Lucas Lucas Lucas
# Lucas Lucas Lucas Lucas Lucas Lucas
# Lucas Lucas Lucas Lucas Lucas Lucas Lucas

um = tuple(range(1, 2))

for each_data in range(1, 8):
    print(um * each_data)

# (1,)
# (1, 1)
# (1, 1, 1)
# (1, 1, 1, 1)
# (1, 1, 1, 1, 1)
# (1, 1, 1, 1, 1, 1)
# (1, 1, 1, 1, 1, 1, 1)

# O que está acontecendo?
nome = 'Lucas '
seq = iter(range(1, 8))
print(nome * next(seq))
print(nome * next(seq))
print(nome * next(seq))
print(nome * next(seq))
print(nome * next(seq))
print(nome * next(seq))
print(nome * next(seq))
"======================================================================================================================"



# n5vnt5531zrkzkoif9dbrnqwushin9hf2lk76ddxpmstkn6v82aad83f1myhse3yruqibmemx7bq6i5hicknvmilshitt6wonb3g
# Loop for: usando lista para coletar dados locais existentes apenas em loop for
"======================================================================================================================"
dicio = {'python': 'string', 1j: 'complexo', False: 'booleano', 81 ** 0.5: 'inteiro'}

lista_externa_ao_loop = []
for dados in dicio.items():
    lista_externa_ao_loop.append(dados)
print(lista_externa_ao_loop)  # [('python', 'string'), (1j, 'complexo'), (False, 'booleano'), (9.0, 'inteiro')]
"======================================================================================================================"



# dzwoptvy7vs7v3pwffyf9ffay5kwisvj5q6nixq8hacb2v9q3kukke1yd2k5dumobeid6cp2t6547fpd165k9zeb8p3nm1ckjses
# Loop while e operador aritmético como gerador de saltos
"======================================================================================================================"
contar = 0
while contar <= 10:
    print('contando: [{}]'.format(contar))
    contar += 2
    # contando: [0]
    # contando: [2]
    # contando: [4]
    # contando: [6]
    # contando: [8]
    # contando: [10]
"======================================================================================================================"



# myf1u9kfrs5qa6ysy6ackee4yv54xdkhr7ngmt58yaoh9xsseh72jjv8avk9ka7cbqgcpx16gu2ppvs6gmqk9w98f8kv6cdefphk
# Multiplicação em iteráveis em [ lista ] [ casting range ] [ string ] [ tupla ]
# [ clonagem de dados ] [ tolerável em lista/string/tupla ]
"======================================================================================================================"
contexto = ('print', 'valor da variável', 'variável própria', 'variável nova')
contexto2 = ('pós-variável',)

# CONJUNTO E DICIONARIO NÃO PERMITEM O USO DE OPERADORES

lista = ['linguagem', 'python'] * 2
print(lista)      # ['linguagem', 'python', 'linguagem', 'python']

range_ = range(1, 8)
range2_ = list(range_) * 2
print(range2_)    # [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7]

string = 'Lucas Farias '
string = string * 3
print(string)     # Lucas Farias Lucas Farias Lucas Farias

tupla = (('1', 1), {2, '2'}, {3.0: None})
print(tupla * 3)  # (('1', 1), {2, '2'}, {3.0: None}, ('1', 1), {2, '2'}, {3.0: None}, ('1', 1), {2, '2'}, {3.0: None})

# USO A MULTIPLICAÇÃO EM UM CONTEXTO DE PÓS-VARIÁVEL
tupla = (2, '', None)
tupla *= 20
print(tupla)
"======================================================================================================================"



# mkv4tadumxnnxloqtx75wioobd9cbctyrskyica1ncypo1da2awijwgdjdxgu7ycwqhyekm2uoxw72laqsig6irnmx6b853p7b7f
# Operador lógico not: substituição de operação relacional completa
"======================================================================================================================"
var = (1, 2, 3, 4, 5)

"Conclusão 1"  # Ou é passado a operação relacional completa
"Conclusão 2"  # Ou é passado a operação relacional incompleta com a presença do operador lógico NOT

for each_data in var:
    if each_data % 2 == 0:         # Nesse caso, a operação relacional está completa
        print(each_data, end=' ')  # 2 4

for each_data in var:
    if each_data % 2:              # Nesse caso, a operação relacional NÃO está completa (operador relacional ausente)
        print(each_data, end=' ')  # 1 3 5

for each_data in var:
    if not each_data % 2:          # Nesse caso, a operação relacional NÃO está completa + operador lógico NOT
        print(each_data, end=' ')  # 2 4
"======================================================================================================================"



# r8qjzomst7xu1bc7rm6fhsbkbi7srkemk8pc6gaqdc933kcyr3clt1jgoiznpf5sle4iqm62kqpkx99jfjc2fe7el1xnyqvk13ld
# Operadores lógicos e as probabilidades de retorno True
# [ probabilidade 25% & 75% ]
"======================================================================================================================"
# 75% [ operador binário ] [ or ]
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

# 25% [ operador binário ] [ and ]
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False
"======================================================================================================================"



# 3ywlzl7tv69g9vn4bxhfnl3rp285bkaqt17ux1e22tx75qw8vy7zuxfgwc9uunc6ae854f4skareoxy17dzqfdzjlywd21uu2ttj
# Tipos de paradigmas de programação
"======================================================================================================================"
# Paradigmas de programação
tipos = "estruturada", "orientada a objeto", "funcional"

# Programação orientada a objeto
"Mapeamento de objetos do mundo real para simulação no mundo virtual [ modelos computacionais ]"

# Observações sobre linguagens em relação aos paradigmas
"1. C não suporta o paradigma de programação orientada a objeto"
"2. Java não suporta o paradigma de programação estruturada"

# Tipos de atributos
atributos = "atributos de instância", "atributos de classe", "atributos dinâmicos"

# Tipos de métodos
metodos = (
    "método de classe",                               # @classmethod
    "método de instância",                            # não há regra
    "método de instância com decorador propriedade",  # @property
    "método de instância com decorador setter"        # @nome da função com @property.setter
    "método estático",                                # @staticmethod (função def)
    "método construtor",                              # __init__
    "método privado",                                 # underline ao fim do nome da função
    )

# Observações sobre atributos de instância
"1. São criados majoritariamente em um método contrutor/inicializador"
"2. Eles funcionam exatamente como parâmetros de um função [ def(): ]"

# Outras observações
"1. Ao criar uma classe, cria-se um objeto, que passa a pertencer a uma nova classe de dados na linguagem Python"
"2. Uma classe = nova classe de dados, que não é integrada à linguagem, por isso sua sintaxe é diferente (Camel case)"
"3. Ao criar uma classe, significa que deseja-se instanciar um ou múltiplos objetos vindo dela"
"4. Classes, quando agrupadas, podem também ser conhecidas como [ entidades ]"
"6. Um objeto é instanciado no (escopo global), mas têm acesso ao (escopo local) da classe que o criou"
"7. Objetos instanciados são variáveis que recebem como valor = nome da classe(valores dos atributos de instância)"


class Notebook:                            # Criação de uma classe com nome: Notebook
    def __init__(self, valor, marca, cor):
        self.__valor = valor
        self.__marca = marca
        self.__cor = cor

asus = Notebook(4567, 'Dell', 'prateado')  # Instanciação de um objeta da classe: Notebook
"======================================================================================================================"



# gjm7m3t488jdo6k1k4og5r1irw768mct83f5dfg1y2l1uc8tiz97tr6hmbijyb7uj293clopqdmolrniimxdv84pl4o8a9tmur83
# Pontilhando casas numéricas [ pequeno algoritmo ]
"======================================================================================================================"
from resources import *
from ansi_colors import *
from error_handling import mistake_at_integer

title = '\nWelcome to the {}Integer dot positioner{}'.format(colors['bold_dodgerblue'], colors['standard'])

ask_for_integer = """
{}{} What is the integer to be dotted? {}{}
1. {}
2. Type the integer number
3. {}
-> """.format('=' * row, colors['bold_white'], colors['standard'], '=' * row, click_arrow, press_enter_key)

print(title)

while True:

    algorithm_action = input(doubt_run_algorithm)
    if algorithm_action in algorithm_cease:
        break

    print(title)

    while True:

        try:

            integer = int(input(ask_for_integer))

            if len(str(integer)) == 7:  # 1234567 -> '.' [1]  '.' [5]

                integer_storage = [each_data for each_data in str(integer)]
                integer_storage.insert(1, '.'), integer_storage.insert(5, '.')
                shaped_integer = ''.join(integer_storage)
                print('\n{}{}{}'.format(colors['bold_dodgerblue'], shaped_integer, colors['standard']))

            elif len(str(integer)) == 6:  # 123456 -> '.' [3]

                integer_storage = [each_data for each_data in str(integer)]
                integer_storage.insert(3, '.')
                shaped_integer = ''.join(integer_storage)
                print('\n{}{}{}'.format(colors['bold_dodgerblue'], shaped_integer, colors['standard']))

            elif len(str(integer)) == 5:  # 12345 -> '.' [2]

                integer_storage = [each_data for each_data in str(integer)]
                integer_storage.insert(2, '.')
                shaped_integer = ''.join(integer_storage)
                print('\n{}{}{}'.format(colors['bold_dodgerblue'], shaped_integer, colors['standard']))

            elif len(str(integer)) == 4:  # 12345 -> '.' [1]

                integer_storage = [each_data for each_data in str(integer)]
                integer_storage.insert(1, '.')
                shaped_integer = ''.join(integer_storage)
                print('\n{}{}{}'.format(colors['bold_dodgerblue'], shaped_integer, colors['standard']))

        except ValueError:

            print(mistake_at_integer)
"======================================================================================================================"



# v3i3aact49znuq4hqzrocel8pt6k6yvpyekte8lgomvxch173l428e39iwz84axbtualjfmykdlyufazewslywk1b919l8mrbmn9
# POO: acessando e usando método de instância
"======================================================================================================================"
class Celular:
    def __init__(self, marca, modelo, cor):
        self.marca = 'Marca do produto: {}'.format(marca)
        self.modelo = 'Modelo do produto: {}'.format(modelo)
        self.cor = 'Cor do produto: {}'.format(cor)

    "Método de instância alterando atributos de instância"
    def cacha_alta(self):
        self.marca = self.marca.upper()
        self.modelo = self.modelo.upper()
        self.cor = self.cor.upper()
        return self.marca, self.modelo, self.cor

asus = Celular('asus', 'xahuan 7j', 'verde')  # objeto = classe(instâncias do objeto)
print(asus.cacha_alta())                      # print(objeto.método de instância())
# ('MARCA DO PRODUTO: ASUS', 'MODELO DO PRODUTO: XAHUAN 7J', 'COR DO PRODUTO: VERDE')

print(Celular.cacha_alta(asus))               # print(classe.método de instância(objeto))
# ('MARCA DO PRODUTO: ASUS', 'MODELO DO PRODUTO: XAHUAN 7J', 'COR DO PRODUTO: VERDE')
"======================================================================================================================"



# 5o42v62xxbx7ryxnt7v36ozj969a9c3os7fwzx9fkrdt9dj5gks8i6spdlcy9r7jz7qi1z53gufv1dkzmvydjgsq92j59toqhk6g
# POO: chamadas de atributos de classe & mesclagem com atributos de instância
"======================================================================================================================"
# Atributos de classe são variáveis, e são criadas anteriores ao método construtor & aos atributos de instância
# Atributos de classe podem interagir com os atributos de instância
class Produto:

    imposto = 0.12  # atributo de classe [ acesso notação ponto ] [ Produto.imposto ]

    def __init__(self, produto, cor, valor):
        self.produto = produto
        self.cor = cor
        self.valor = valor + (valor * Produto.imposto)

ps4 = Produto('playstation 4 oblivion', 'prateadofosco', 3419.27)
print(ps4.imposto)      # 0.12   # forma incorreta de chamar um atributo de classe [ objeto.atributo de classe ]
print(Produto.imposto)  # 0.12   # forma correta de chamar um atributo de classe   [ classe.atributo de classe ]
"======================================================================================================================"



# 746425wz92qcve4zlm3n59rbmh2621r9xeote28rbmhou489zw926liiiirainnpjwhuu7s8qay6xbtrjabspfpprb9nod3dc4ps
# POO: atributo de instância & name mangling
"======================================================================================================================"
# Observações
"1. Atributos, de uma forma geral, são de privacidade pública [ self.atributo ]"
"2. Porém, [ double_dunder ] torna-o de privacidade privada [ self.__atributo ]"
"3. O nível de acesso [ público ] & [ privado ] é uma convenção, pois é possível acessar atributo(s) [ privado(s) ]"
"4. O ato de acessar atributos privados chama-se [ name mangling ]"


class Controle:                         # criação de uma classe
    def __init__(self, volume, canal):  # criação/chamada de atributos
        self.volume = volume            # definição dos atributos
        self.canal = canal              # atributo [ público ] ausente de [ double_dunder ]
        self.mutar = None

var = Controle(72, 5)                   # criação de um objeto da classe   # definição das instâncias do objeto
print(var.canal)                        # acesso objeto.atributo de instância público


class Controle2:
    def __init__(self, brilho, contraste):
        self.__brilho = brilho          # atributo [ privado ] com [ double_dunder ]
        self.__contraste = contraste
        self.__mutar = 'indisponível'

var2 = Controle2(100, 44)
print(var2._Controle2__brilho)  # [ name_mangling ]
                                # acesso a atributo [ privado ] [ objeto_classe__atributo ] [ OCA ]
"======================================================================================================================"



# jrua6fbr9flxbtnk935hkp3ajuuxigj21px4f44cgcnqny3d4xoqw2jcka6jzvnq7foeufnwzb31iv543cxz41tatcijt8ngtr15
# POO: atributo dinâmico
"======================================================================================================================"
# Atributo dinâmico é um tipo de atributo que normalmente é criado após a criação do objeto [ apesar de incomum ]
# Esse tipo de atributo existe somente no objeto que foi criado, caso contrário, [ AttributeError ]
# Ao mesmo tempo que é chamado, precisa ser também definido
class Bdd:

    def __init__(self, nome, idade, pais):
        self.__nome = nome
        self.__idade = idade
        self.__pais = pais

user = Bdd('Hamah', 44, 'Irã')
print(user.__dict__)       # {'_Bdd__nome': 'Hamah', '_Bdd__idade': 44, '_Bdd__pais': 'Irã'}
user.__sexo = 'masculino'  # atributo dinâmico criado aqui
print(user.__dict__)       # {'_Bdd__nome': 'Hamah', '_Bdd__idade': 44, '_Bdd__pais': 'Irã', '__sexo': 'masculino'}
                           # Atributo dinâmico [__sexo] não recebe a instância da classe [_Bdd], pois não é parte dela

"Tentativa de chamar atributo dinâmico pela classe (sem sucesso)"
# print(user._Bdd_sexo)      # AttributeError: 'Bdd' object has no attribute '_Bdd_sexo'

"A única forma de acesso é pelo OBJETO INSTÂNCIADO"
print(user.__sexo)           # masculino
"======================================================================================================================"



# 4ro3iypsk3rluvbd13cscktikzwg6dg1y4vmkdamwjn5xph29bh2hodomxnisp9grsuxduekdfwy37o9rgxbn7ss4alv2n8rmggy
# POO: deletando atributo de instância do objeto, gerando dicionário do objeto para provar instância deletada
"======================================================================================================================"
class Bandeira:
    def __init__(self, altura, cores, largura):
        self.altura = altura
        self.cores = cores
        self.largura = largura

argentina = Bandeira(20, ('azul claro', 'branco'), 60)
var = argentina.__dict__
print(var)  # {'altura': 20, 'cores': ('azul claro', 'branco'), 'largura': 60}
del argentina.altura  # 'altura': 20 será excluido
print(var)  # {'cores': ('azul claro', 'branco'), 'largura': 60}
"======================================================================================================================"



# b2lovffkst9z7cam4cunxov81rvtj1trofaee3ay1avlro6owpmo8uszoba7japyo11emqkv7bkk11um59wgqvm13p7kuvex9db1
# POO: demonstração abrangente de recursos
"======================================================================================================================"
from passlib.hash import pbkdf2_sha256 as crypto  # importação de criptografia


class Var:                            # declaração de classe, também conhecido como entidade

    ano = 2020                        # atributo de classe [ OBS ] criado externo ao método inicializador/construtor
    continente = ' (América do sul)'  # atributo de classe [ OBS ] também conhecido como atributo estático
    contar = 0

    @classmethod        # [ @classmethod ] [ OBS ] pode haver um método de classe para cada atributo de classe
    def mtd_cls(cls):   # [ @classmethod ] [ OBS ] parâmetro [ cls ] é convencional, podendo ser outro nome
        print(cls.ano)  # [ @classmethod ] [ OBS ] aceita como ação: [ print ] ou [ return ]

    @classmethod                    # [ @classmethod ] é um decorador mandatório para gerenciar atributos de classe
    def mudar_ano(cls, alterador):  # Isso é um método específico para alterar um atributo de classe, caso necessário
        cls.ano = alterador

    @staticmethod                   # [ @staticmethod ] é um decorador mandatório para a chamada de funções normais
    def frase():                    # [ @staticmethod ] não é feito para interagir com atributos de forma geral
        return 'Método estático é uma função normal com nome enfeitado por um decorador, {}'

    def __init__(self, pais, idioma, nascimento, key):  # método construtor(self, atributo de instância):

        self.id = Var.contar + 1           # atributo de instância [ não inicilizado ] [ público ]
        self.nascimento = nascimento       # atributo de instância [ inicializado ] [ público ]
        self.pais = pais
        self.pais = pais + Var.continente  # atributo de instância [ inicializado ] [ público ] [ redefinido ]
        self.__idioma = idioma             # atributo de instância [ inicializado ] [ privado ]
        self.__key = crypto.hash(key, rounds=200_000, salt_size=16)  # atributo de instância [ criptografia ]
        Var.contar = self.id                                         # atributo de classe redefinido
        print(self.__lista_idioma())       # método privado impresso
        # self.pais = pais[::-1].upper().split()
        # print(self.pais)

    def mtd_inst(self):                 # método de instância [ OBS ] mandatório a presença de atributo(s) de instância
        print('-'.join(self.__idioma))  # [ OBS ] dois tipos de ação: [ print ] ou [ return ]

    def pais_destaque(self):  # método de instância [ OBS ] pode haver um [ mtd de inst. ] para cada [ atr de inst. ]
        print('{}{}{}'.format('\033[1:34m', self.pais.upper(), '\033[0:37m'))  # ação do método de instância

    def pais_idade(self):  # método de instância
        print('{}{} anos{}'.format('\033[1:34m', Var.ano - self.nascimento, '\033[0:37m'))

    def __lista_idioma(self):
        return self.__idioma.split()

# Objetos de instância [ var ] [ var2 ] [ var3 ]
var = Var('Brasil', 'português', 1500, 'bra')  # [ OBS ] pode haver múltiplos de uma classe
var2 = Var('Argentina', 'espanhol', 0, 'arg')  # [ OBS ] parâmetros preenchidos = valores dos atributos de instância
var3 = Var('Holanda', 'holandês', 0, 'hol')    # [ OBS ] parâmetros preenchidos são chamados de [ instância/objeto ]

var.estado = 'Piauí'                           # atributo dinâmico [ OBS ] existe apenas no objeto onde foi criado
                                               # pode ser passado como atributo privado, mas é desnecessário, pois:
                                               # 1. Não há acesso por [ name_mangling ] atributos privados
                                               # 2. Não há acesso por método de instância [ ele não existe na classe ]
                                               # 3. O único acesso é por dicionário do objeto instanciado

var.mtd_cls()                                  # objeto.método de classe
var.mtd_inst()                                 # objeto.método de instância
var.pais_destaque()                            # objeto.método de instância
var.pais_idade()                               # objeto.método de instância
Var.pais_idade(var)                            # classe.método de instância(objeto) [ sintaxe estranha ]

print(dir(var))                                # acesso à métodos disponíveis para objetos de classe/instância
print(var.pais)                                # objeto.atributo de instância [ OBS ] acesso específico
print(Var.continente)                          # classe.atributo de classe
print(var._Var__key)                           # objeto._classe__atributo privado [ OBS ] acesso atr.inst. privado
print(var.id, var.pais, var._Var__idioma)      # atributos de instância [ OBS ] chamada menos eficiente
print(var.__dict__)                            # atributos de instância [ OBS ] chamada mais eficiente [ dicionário ]
print(var2.__dict__)                           # atributos de instância [ OBS ] objeto de classe recebendo método
print(var3.__dict__)                           # atributos de instância [ OBS ] o método cria um dicionário
print(var.frase())                             # objeto.método. método estático
del var.estado                                 # deletar instância específica de um objeto

"Ausência de 1+ instâncias:"                         # TypeError: __init__() missing 1 required positional argument: ''
"Acesso de atributo de instância privado incorreto"  # AttributeError: 'Var' object has no attribute 'idioma'
"Métodos de classe são anteriores ao método inicializador/construtor"
"Métodos privados recebem somente atributos de instância privados"
"======================================================================================================================"



# vqmewn22fwvsfh7ufmlsidwxvqo79aef8sisunxv1wiswcj7y4osjxdcfnvz2vcnnuklbqblwhzmp6sbtmk5r2bdmxqx6vwxbmts
# POO: demonstração básica [ classe sem propriedade ] vs [ classe com propriedade ]
# Propriedade: decorador passado acima de um método de instância com objetivo de acessá-lo [ @property ]
# Setter:      decorador passado acima de um método de instância com objetivo de alterá-lo [ @nome.setter ]
"======================================================================================================================"
# Quais as diferenças?

# 1. Métodos de instância comuns são criados pós método construtor
# 2. Métodos de instância comuns dependem de parênteses na chamada com o objeto instânciado
# 3. Métodos de instância comuns altera o atributo de instância por função passando argumento, que será o novo valor

# 1. Métodos de instância com decorador propriedade são criados pré método construtor (convenção, não mandatório)
# 2. Métodos de instância com decorador propriedade dispensam parênteses
# 3. Métodos de instância com decorador propriedade altera atributo de instância por declaração de uma variável


class Time:

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def simbolo(self):
        return self.__simbolo

    @simbolo.setter
    def simbolo(self, novo_simbolo):
        self.__simbolo = novo_simbolo

    def __init__(self, nome, simbolo):
        self.__nome = nome
        self.__simbolo = simbolo

    def chamar_nome(self):
        return self.__nome

    def chamar_simbolo(self):
        return self.__simbolo

    def alterar_nome(self, novo_nome):
        self.__nome = novo_nome

    def alterar_simbolo(self, novo_simbolo):
        self.__simbolo = novo_simbolo

var = Time('Flamengo', 'Urubu')  # Instânciação do objeto

print(var.chamar_nome())       # Método de instância comum (parênteses = mandatório)
print(var.chamar_simbolo())    # Método de instância comum (parênteses = mandatório)
var.alterar_nome('Palmeiras')  # Método de instância alterador comum (chamada de função com argumento)
var.alterar_simbolo('Porco')   # Método de instância alterador comum (chamada de função com argumento)

print(var.nome)                # Método de instância com decorador de propriedade (parênteses = dispensável)
print(var.simbolo)             # Método de instância com decorador de propriedade (parênteses = dispensável)
var.nome = 'Cruzeiro'          # Método de instância alterador com propriedade @nome.setter (declaração)
var.simbolo = 'Raposa'         # Método de instância alterador com propriedade @nome.setter (declaração)

print(var.nome)
print(var.simbolo)
"======================================================================================================================"



# auat99zho963qdr4zsfay8t9yoz8x232dt1hyjynyf2jdeyp4v4shqoxvhf79pioqt2cozo7xrqa59isr73xwcd24eb4okqiyqq2
# POO: exemplo de algoritmo [ atributos de instâncias privados = encapsulamento de dados ]
"======================================================================================================================"
"""
Qual a relação da Programação orientada a objeto com encapsulamento?
1. Está voltada ao encapsulamento de código em um grupo lógico e hierárquico, usando para isso, classes
2. Abstração é o processo de esconder etapas do código que são desnecessárias do usuário ter conhecimento. Um exemplo
seria o ato de ligar para outra pessoa, a abstração está no usuário não precisar saber que, ao efetuar uma chamada,
o seu celular acessa um banco de dados de uma operadora e cria uma conexão de ponto para tornar possível a comuniação
entre os números envolvidos
"""

from resources import *
from ansi_colors import *
from error_handling import mistake_at_float


class Account:

    id_counter = 0
    extract_amount = None
    storage_amount = None

    client_extract = """
{}{} Client extract {}{}
Registry number: {}
Holder: {}
Current balance: {} U$ dollars
Current limit: {} U$ dollars
"""

    ask_for_amount = """
{}{} How much do you want to store to your account? {}{}
1. {}
2. Type the amount of money to be stored
3. {}
-> """.format('=' * row, colors['bold_white'], colors['standard'], '=' * row, click_arrow, press_enter_key)

    ask_for_extraction = """
{}{} How much do you wish to take from your account? {}{}
1. {}
2. Type the amount of money to be stored
3. {}
-> """.format('=' * row, colors['bold_white'], colors['standard'], '=' * row, click_arrow, press_enter_key)

    invalid_storage = """
{}{} Error found {}{}
{}The value to be stored must be positive ( + ), not negative ( - ){}
    """.format('=' * row, colors['bold_crimson'], colors['standard'], '=' * row, colors['crimson'], colors['standard'])

    unauthorized_extraction = """
{}{} Error found {}{}
Current extract limit at once: [ {}{}{} U$ dollars ]
{}Extraction permitted:{} [ equals ] or [ less ] than the holder's current extract limit
{}Extraction denied:{} [ zero ] or [ above ] the holder's current extract limit
    """

    balance_decrement_report = """
{}{} Client balance decrement report {}{}
Current holder's balance has been downgraded to [ {}{}{} U$ dollars ]
    """

    balance_increment_report = """
{}{} Client balance increment report {}{}
Current holder's balance has been upgraded to [ {}{}{} U$ dollars ]
        """

    def __init__(self, holder, balance, limit):

        self.id_counter = Account.id_counter + 1
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit
        Account.id_counter += 1

    def extract_checkage(self):

        return Account.client_extract.format('=' * row, colors['bold_dodgerblue'], colors['standard'], '=' * row,
                                             self.id_counter, self.__holder, self.__balance, self.__limit)

    def storage(self):

        while True:

            algorithm_action = input(doubt_run_algorithm)

            if algorithm_action in algorithm_cease:

                break

            while True:

                try:

                    print(clt.extract_checkage())

                    Account.storage_amount = float(input(Account.ask_for_amount))

                    if Account.storage_amount > 0:

                        self.__balance += Account.storage_amount

                        print(Account.balance_increment_report.format('=' * row, colors['bold_dodgerblue'],
                                                                      colors['standard'], '=' * row,
                                                                      colors['bold_dodgerblue'], self.__balance,
                                                                      colors['standard']))

                        break

                    else:

                        print(Account.invalid_storage)

                except ValueError:

                    print(mistake_at_float)

    def extract(self):

        while True:

            algorithm_action = input(doubt_run_algorithm)

            if algorithm_action in algorithm_cease:

                break

            while True:

                try:

                    print(clt.extract_checkage())

                    Account.extract_amount = float(input(Account.ask_for_extraction))
                    if 0 < Account.extract_amount <= self.__limit:


                        self.__balance -= Account.extract_amount

                        print(Account.balance_decrement_report.format('=' * row, colors['bold_crimson'],
                                                                      colors['standard'], '=' * row,
                                                                      colors['bold_crimson'], self.__balance,
                                                                      colors['standard']))

                        break


                    else:

                        print(Account.unauthorized_extraction.format('=' * row, colors['bold_crimson'],
                                                                     colors['standard'], '=' * row,
                                                                     colors['bold_crimson'], self.__limit,
                                                                     colors['standard'], colors['bold_dodgerblue'],
                                                                     colors['standard'], colors['bold_crimson'],
                                                                     colors['standard']))

                except ValueError:

                    print(mistake_at_float)

"Criação de objetos"
clt = Account('Lucas', 5220, 700)
clt2 = Account('Alfredo', 4400, 900)

"Teste dos métodos de instância [ ative e desative para testar ]"
# print(clt.extract_checkage())
# clt.storage()
# clt.extract()
# print(clt.extract_checkage())

"Acessando atributo de instância privado e modificando-o"
# 1. Inicialmente, [ self.__holder ] da 1ª instância do objeto [ clt ] é = 'Lucas'
print(clt.extract_checkage())
# 2. Acessa-se esse [ objeto ] [ clt ] pela sua classe [ Account ] e o atributo de instância privado [ self.__holder ]
# 2.2 O acesso é feito através da sintaxe [ name mangling ]
# 2.3 Portanto, [ self.__holder ] sofre uma reatribuição
clt._Account__holder = 'Rodolfo'
# 3. Antes, [ self.__holder ] = 'Lucas'
# 3.2 Depois, [ self.__holder ] = 'Rodolfo'
print(clt.extract_checkage())
"======================================================================================================================"



# a8ora86322aodgj41i633lsg66yls5peusxvtjawzldkqratbygwqqh84wv1hvbgdztebzkfada3n11g4uy7y7wmaxzp1dz4gncm
# POO: exemplo simples de métodos de instância
"======================================================================================================================"
from ansi_colors import *


class Conta:
    linha = 15
    id = 0
    dados_cliente = """
{}{} Dados do cliente {}{}
1. Nome do titular: [ {} ]
2. Saldo:           [ {} ]
3. Limite:          [ {} ]
        """

    def __init__(self, titular, saldo, limite):
        self.id = Conta.id + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.id = self.id

    def extrato(self):
        print(Conta.dados_cliente.format('=' * Conta.linha, colors['bold_dodgerblue'], colors['standard'],
                                         '=' * Conta.linha, self.__titular, self.__saldo, self.__limite))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, conta_destino):
        self.__saldo -= valor
        conta_destino.__saldo += valor
        print('Foi retirado uma quantia de R$ {} da conta [ {} ]'.format(valor, self.__titular))

cliente_lucas = Conta('Lucas', 3100, 1200)
cliente_alfredo = Conta('Alfredo', 3900, 1500)

cliente_lucas.extrato()
cliente_lucas.transferir(100, cliente_alfredo)
cliente_lucas.extrato()
"======================================================================================================================"



# w4ow3hbybm6bq35qmmn5tyvsjdchrqitj6i8s5664wl16nfsnmaoth9bjffrzm8wqu38mhlamvqokz3qvw9ehjvykuw978bj6ejd
# POO: Herança
"======================================================================================================================"
"1. Herança é a criação de uma classe matriz, cujos atributos de instância e outros recursos podem ser herdados"
"2. A classe que recebe a herança, pode escolher qual(is) atributos de instância serão herdados da classe matriz"
"3. As classes que recebem a herança são chamadas de classe filha/sub-classe"
"4. Como se faz a herança?"
"5. class NomeDaClasseFilha(NomeDaClasseMatriz):"
"6. Ao executar herança, torna-se obrigatório o uso da super função [ super() ] nas classes influenciadas"
"7. Super função [ super().__init__() ] não leva [ self ] consigo, a não ser que:                        [ ver abaixo ]"
"8. [ super().__init__() ] seja substituido pelo nome da classe e self passe a ser integrado             [ ver abaixo ]"
"9. [ super().__init__(name, last_name, itr) ] torna-se [ ClasseMatriz.__init__(self, nome, sobrenome, cpf) ]"


class ClasseMatriz:
    linha = '=' * 15
    tipo_dado = ('cliente', 'renda', 'empregado', 'registro')
    dados = """
    {} Dados do {} {}
    1. Nome do titular: {}
    2. Sobrenome do titular: {}
    3. {} do titular: {} 
    """

    def __init__(self, nome, sobrenome, cpf):  # todos os atributos de instância aqui genéricos
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf                       # itr significa (individual taxpayer registration)

    def dados_cliente_empregado(self):         # o [ self ] indica que haverá o uso de atributos de instância
        print(ClasseMatriz.dados)


class Cliente(ClasseMatriz):                          # classe recebendo herança da classe matriz

    def __init__(self, nome, sobrenome, cpf, renda):  # os atributos de instância ainda são passados
        super().__init__(nome, sobrenome, cpf)        # super função dentro do método construtor da classe influenciada
        self.__renda = renda                          # atributos de instância não herdados devem ser inicializados

    # O método de instância abaixo também pode ser herdado, e sua chamada deve ter o mesmo nome
    # O método de instância abaixo está [ sobescrevendo ] o método de instância da classe matriz
    # Uma forma de chamar o atributo de instância genérico é usando [ name mangling ] [ _ClasseMatriz__atr. de inst. ]
    # Para chamar o atributo de instância da própria classe, usa-se [ self ] comum
    def dados_cliente_empregado(self):
        print(ClasseMatriz.dados.format(ClasseMatriz.linha,
                                        ClasseMatriz.tipo_dado[0],      # atributo de classe herdado
                                        ClasseMatriz.linha,
                                        self._ClasseMatriz__nome,       # atributo de instância herdado [ name_mangling ]
                                        self._ClasseMatriz__sobrenome,  # atributo de instância herdado [ name_mangling ]
                                        ClasseMatriz.tipo_dado[1],      # atributo de classe herdado
                                        self.__renda))                  # atributo de instância não herdado


class Empregado(ClasseMatriz):
    def __init__(self, nome, sobrenome, cpf, registro):
        super().__init__(nome, sobrenome, cpf)
        self.__registro = registro

    def dados_cliente_empregado(self):
        print(ClasseMatriz.dados.format(ClasseMatriz.linha,
                                        ClasseMatriz.tipo_dado[2],      # atributo de classe herdado
                                        ClasseMatriz.linha,
                                        self._ClasseMatriz__nome,       # atributo de instância herdado [ name_mangling ]
                                        self._ClasseMatriz__sobrenome,  # atributo de instância herdado [ name_mangling ]
                                        ClasseMatriz.tipo_dado[3],      # atributo de classe herdado
                                        self.__registro))               # atributo de instância não herdado

cliente1 = Cliente('Rubson', 'Fagundes', '139.904.112-07', 4327)
empregado1 = Empregado('Jan', 'Bills', '102.098.444-10', 2104)

"1. Atributo de instância da classe [ ClasseMatriz ] [ herdado ]"
"2. Atributo de instância da classe [ Cliente ]"
cliente1.dados_cliente_empregado()
# =============== Dados do cliente ===============
# 1. Nome do titular: Rubson
# 2. Renda do títular: 4327


empregado1.dados_cliente_empregado()
# =============== Dados do empregado ===============
# 1. Nome do titular: Jan
# 2. Sobrenome do titular: Bills
# 3. registro do titular: 2104
"======================================================================================================================"



# 7fii3974a6xcwn1ynb3s55wy1wgugiyy9gpmn7cbq17wyzbo3mi6fq8yvc2mkdhl2vs5wz53pnsmlhh768yg8xszmmkl9r4vfy6l
# POO: herança múltipla [ derivação direta ] [ derivação indireta ]
"======================================================================================================================"
"Derivação direta"    # é quando uma classe neto, recebe herança do nome do pai, ao invés do nome do avô
"Derivação indireta"  # é a classe avô, sendo chamada indiretamente pela chamada da classe pai no nome da classe filha


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def apresentar(self):  # Método de instância regular [ será sobescrito pelas classes herdadas ]
        print('Nome do animal {}'.format(self.__nome))


class Ar(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def apresentar(self):  # Método de instância herdado da classe [ Animal ] que está sendo sobescrito
        print('Nome do animal aéreo: {}'.format(self._Animal__nome))


class Mar(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def apresentar(self):  # Método de instância herdado da classe [ Animal ] que está sendo sobescrito
        print('Nome do animal marinho: {}'.format(self._Animal__nome))


class Terra(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def apresentar(self):  # Método de instância herdado da classe [ Animal ] que está sendo sobescrito
        print('Nome do animal terrestre: {}'.format(self._Animal__nome))


class Hibrido(Terra, Mar):

    def __init__(self, nome):
        super().__init__(nome)


papagaio = Ar('Juvêncio')
cavalo_marinho = Mar('Cubicuz')
tatu_bola = Terra('Armadilo')
pinguim = Hibrido('Jubeleu')

pinguim.apresentar()          # a classe [ Híbrido ] herda tudo da classe [ Terra, Mar ] & [ Animal ]
print(pinguim._Animal__nome)  # o objeto [ pinguim ] só consegue acessar por [ name mangling ], o seu atributo
                              # de instância [ self.__nome ] pela classe avô [ Animal ]

"Toda herança, por mais terceirizada que seja, gera acesso entre as classes envolvidas, até chegar à classe matriz"
"A classe [ Híbrido ] não possui métodos de instância, mas pode facilmente ser acessado de classes herdadas"
"De qual das classes a classe [ Hibrido ] herdaria o método de instância, então?"
# A classe [ Hibrido ] recebe direvação direta das classes [ Mar & Terra ], portanto, de uma das duas
"Mas, qual?"
# O nome da classe que for passada primeiro na herança, portanto, o método de instância da classe [ Terra ]
pinguim.apresentar()  #

print(isinstance(pinguim, Ar))       # False
print(isinstance(pinguim, Mar))      # True
print(isinstance(pinguim, Terra))    # True
print(isinstance(pinguim, Hibrido))  # True
print(isinstance(pinguim, object))   # True
"======================================================================================================================"



# 1yjoylekn8lid64ghcbeuvl4vhqwysqdai38akunyme8ntdew5zbi2cqou13okd1bl6tdwdb9dykila7tee896ifrfmmhya26ic9
# POO: method resolution order
# [ criador de dicionário contendo ordem de precedência de herança das classes ]
"======================================================================================================================"
class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def apresentar(self):  # Método de instância regular [ será sobescrito pelas classes herdadas ]
        print('Nome do animal {}'.format(self.__nome))


class Ar(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def apresentar(self):  # Método de instância herdado da classe [ Animal ] que está sendo sobescrito
        print('Nome do animal aéreo: {}'.format(self._Animal__nome))


class Mar(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def apresentar(self):  # Método de instância herdado da classe [ Animal ] que está sendo sobescrito
        print('Nome do animal marinho: {}'.format(self._Animal__nome))


class Terra(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def apresentar(self):  # Método de instância herdado da classe [ Animal ] que está sendo sobescrito
        print('Nome do animal terrestre: {}'.format(self._Animal__nome))


class Hibrido(Terra, Mar):

    def __init__(self, nome):
        super().__init__(nome)

sapo = Hibrido('Sapo')
print(Hibrido.__mro__)  # (<class '__main__.Hibrido'>, <class '__main__.Terra'>, <class '__main__.Mar'>, <class '__main__.Animal'>, <class 'object'>)
print(Hibrido.mro())    # [<class '__main__.Hibrido'>, <class '__main__.Terra'>, <class '__main__.Mar'>, <class '__main__.Animal'>, <class 'object'>]
help(Hibrido)

# Help on class Hibrido in module __main__:
#
# class Hibrido(Terra, Mar)
#  |  Hibrido(nome)
#  |
#  |  Method resolution order:
#  |      Hibrido
#  |      Terra
#  |      Mar
#  |      Animal
#  |      builtins.object
"======================================================================================================================"



# ryocprkacxe5k2atp6ezc62dpbmiywgnzgfojkscri55mbfncfwazseiy7sxvdjwgvk3pc2st8pujz7jvnbkxw23cblrial4j16k
# POO: Poliforfismo
# Conceito de polimorfismo & erro de não implementação
"======================================================================================================================"
# O que é o [ polimorfismo ]?
"Significa múltiplas formas, ou seja, em POO, são múltiplas formas de fazer uma mesma ação"
"É um nome sofisticado para [ sobescrita = overriding ]"
# Por exemplo:
"Pegando os exemplos abaixo:"
"Uma classe [ Animal ] pode ter vários tipos de animais"
"Em uma classe [ Animal ] todos podem fazer som, porém, cada som é diferente"
"O poliformismo, nesse contexto, é que todos recebem a ação/método de reproduzir um som, mas todos o fazem diferente"


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def som(self):  # Isso aqui é chamado de método abstrato
        # Levantando esse erro, ele torna obrigatório a implementação desse método nas classe com herança
        # Caso contrário: [ NotImplementedError ]
        raise NotImplementedError('Não é possível')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    @property
    def som(self):
        return '{} faz o som: - au au au!'.format(self._Animal__nome)


class Gato(Animal):  # A classe já é avisada de não estar recebendo [ método abstrato ]
    def __init__(self, nome):
        super().__init__(nome)

    # def som(self):
    #     return '{} faz o som: - Miau...miau!'.format(self._Animal__nome)

lucifer = Gato('Lúcifer')
malignus = Cachorro('Malignus')
print(malignus.som)
print(lucifer.som())  # NotImplementedError: Não é possível
"======================================================================================================================"



# ibudayb9jxfwfzy8keoy59wwczlpoznsn2w7vtq21b7ma6llv9qnc5yfbsgxvqwp7d5yibgcz8x3hpb48cpwyxbawwd3m3ogyoap
# POO: [ problema ] atributos de instância públicos permitindo sua alteração no escopo global
"======================================================================================================================"
class Lamp:

    id = 0

    def __init__(self, name, color, voltage, brightness):

        self.id = Lamp.id + 1
        self.name = name  # self.__name = name_________________________________________________________________________
        self.color = color
        self.voltage = voltage
        self.brightness = brightness
        Lamp.id = self.id
        self.lamp_status = False

    def lamp_status_checker(self):
        return self.lamp_status


    def lamp_turnon_turnoff(self):
        if self.lamp_status:
            self.lamp_status = False
        else:
            self.lamp_status = True

lamp1 = Lamp('x', 'red', 220, 80)
print(lamp1.name)  # x

"No escopo global, uma variável pode alterar o atributo de instância de uma classe no seu escopo local"
"Qual a consequência? o atributo de instância perde a instância dada a ele no objeto da classe"
"[ self.__name ] = x muda = y"
name = 'y'
lamp1.name = name  # objeto.atributo de instância = var externa global
print(lamp1.name)  # y

"Se o atributo de instância fosse privado, isso não seria possível [ observe os underlines acima ]"
"[ self.__name ] continua = x"
lamp1 = Lamp('x', 'red', 220, 80)
print(lamp1._Lamp__name)  # x
name = 'y'
lamp1.__name = name
print(lamp1._Lamp__name)  # x
"======================================================================================================================"



# tdm7hjhwdx9bsatp52e7ytawxmw1aeq7rzld9i6ifj6gkvf14ycqo45a35lzwwwr7q7abvi17y97bybm9is78eztapyq2hpt3cgq
# POO: [ problema ] objeto de classe sendo usado como instância de outro objeto de classe
"======================================================================================================================"
"Observar os passos de 1 até 10"

class Cliente:

    def __init__(self, nome, identidade, cpf):
        self.__nome = nome    # 5. O atributo de instância [nome], parece ser o mais adequado para clonagem
        self.__identidade = identidade
        self.__cpf = cpf


class Conta:

    @property
    def cliente(self):  # 6. O atributo de instância [nome] é visível por um método de instância com decorador
        return self.__cliente._Cliente__nome  # self.__objeto._Classe vínculada__atributo de instância vinculado

    def __init__(self, cliente, limite, saque):
        self.__cliente = cliente
        self.limite = limite
        self.saque = saque

    def mostrar_cliente(self):  # 6. O atributo de instância [nome] é visível por um método de instância comum
        print(self.__cliente._Cliente__nome)  # self.__objeto._Classe vínculada__atributo de instância vinculado

    def exibir_cliente(self):
        print(self.__cliente)

pessoa = Cliente('Rodolfo', '1020356', '019.702.114-01')

conta = Conta(pessoa, 1200, 7000)  # 1. algo estranho acontece aqui (um objeto está sendo passado dentro de outro)
                                   # 2. [ pessoa ] é um objeto, e possui três valores, mas apenas um pode ser pego
                                   # 3. ao receber [ pessoa ], cria-se um vínculo entre as duas classes distintas
                                   # 4. é preciso clonar algum atributo de instância da classe [Cliente] para [Conta]

# 7 O objeto [conta] recebeu o objeto [pessoa], mas não está correto
# 8 Então, foi preciso pegar apenas 1 atributo de instância do objeto [pessoa] para dar certo
# 9 O atributo de instância do objeto [pessoa] escolhido, foi: self.__nome
# 10 Portanto: classe Cliente self.__nome = classe Conta self.__cliente
"self.__cliente não é visível pelo método .__dict__"
print(conta.__dict__)  # {'_Conta__cliente': <__main__.Cliente object at 0x03011F70>, 'limite': 1200, 'saque': 7000}

"self.__cliente não é visível por name mangling"
print(conta._Conta__cliente)  # <__main__.Cliente object at 0x03681F70>

"self.__cliente é visível pelo método de instância comum"
conta.mostrar_cliente()       # Rodolfo

"self.__cliente é visível pelo método de instância com decorador de propriedade"
print(conta.cliente)          # Rodolfo
"======================================================================================================================"



# f8uweiass9omxcsffxvjvfrtksm2s9og4zm6zb4ds2er5xnwga6upwnfm5d1jozrq2bmg3jl4dbo9ocb1sknk8y8iwcxpu4k4ed1
# POO: teste de senha com método de instância e exemplos de algoritmos com checagem de senha
"======================================================================================================================"
from passlib.hash import pbkdf2_sha256 as crypt


class Login:
    def __init__(self, user_first_name, user_last_name, user_email, user_key):
        self.__user_first_name = user_first_name
        self.__user_last_name = user_last_name
        self.__user_email = user_email
        self.__user_key = crypt.hash(user_key, rounds=200_000, salt_size=16)

    def key_checkage(self, data_key):
        if crypt.verify(data_key, self.__user_key):  # crypt.verify(par, atr. inst.)  # método.método(par, atr. inst.)
            return self.__user_key
        return False


pessoa = Login('luuk_', 'fazul', 'x_x_lucas@zip.dot', 'bola_drag_2020')
print(pessoa.key_checkage('bola_drag_2000'))  # senha incorreta  # objeto.método de instância('instância')
print(pessoa.key_checkage('bol_drag_2020'))  # senha correta

# Checagem de senha [ forma 1 ]
"Verifica-se na condição se a senha e sua repetição são idênticas"
"Caso sim, um objeto e recebe como instância todas as entradas fornecidas"

name = input('Type name -> ')
last_name = input('Type last name -> ')
email = input('Type email -> ')
key = input('Type key -> ')
key_verify = input('Type key again -> ')

if key == key_verify:
    user = Login(name, last_name, email, key)
    print('The two keys match, access granted!\nCrypted key: {}'.format(user.key_checkage(key)))
else:
    print('Access denied!')

# Checagem de senha [ forma 2 ]
"O objeto já é criado diretamente com as entradas como suas instâncias"
"O objeto chama o método de instância, que possui um parâmetro, esse parâmetro é a instância da senha"

name2 = input('Type name -> ')
last_name2 = input('Type last name -> ')
email2 = input('Type email -> ')
key2 = input('Type key -> ')
key_verify2 = input('Type key again -> ')

user2 = Login(name2, last_name2, email2, key2)

if user2.key_checkage(key2):  # objeto.método de instância(par = 1 instância do objeto)
    print('The two keys match, access granted!\nCrypted key: {}'.format(user2.key_checkage(key)))
else:
    print('Access denied!')
"======================================================================================================================"



# t9g32u4imc2inimegon7y5nfmv2yjg42c9k7pym4ied7cod8vqu8askm5t4ktzk9uloptctqnlk6egoc4tu4ht4xtqgdw5av8sbn
# Pyautogui: gerenciamento de movimentação de mouse nas coordenadas x & y
"======================================================================================================================"
# Coordenada x [ 1º argumento ] [ movimentos horizontais ]
" x "  # se for um valor positivo [ movimento para a direita ]
" x "  # se for um valor negativo [ movimento para a esquerda ]

# Coordenada y [ 2º argumento ] [ movimentos verticais ]
" y "  # se for um valor positivo [ movimento para baixo ]
" y "  # se for um valor negativo [ movimento para cima ]

from pyautogui import hotkey, moveTo

make_cross = [
    hotkey('win', 'd'), moveTo(500, 500, 0.5), moveTo(500, 400, 0.5), moveTo(500, 500, 0.5), moveTo(600, 500, 0.5),
    moveTo(500, 500, 0.5), moveTo(500, 600, 0.5), moveTo(500, 500, 0.5), moveTo(400, 500, 0.5), moveTo(500, 500, 0.5)
]

for each_coordinate in make_cross:
    print(each_coordinate)
"======================================================================================================================"



# ull4xu1yeharya4et8idowx6egxoormbxd18holm7pvvgubrlczuq94yr8o3o2hkyi1abousj7eed9niwtoh3p7f56iuylwai4hp
# Quebra & salto de linha
# [ caractere de escape ] [ separador de conteúdo ] [ distanciador de conteúdo ] [ tipos de string ]
"======================================================================================================================"
print('Quebra de linha é o descolacamento de um conteúdo para a linha abaixo')
print('Salto de linha é o espaçamento de um conteúdo para outro de uma linha em branco')

print('\n')    # Quebra de linha
print('\n\n')  # Salto de linha

quebra_de_linha = 'quebra\nde\nlinha'
print(quebra_de_linha)
# quebra
# de
# linha

quebra_de_linha2 = """quebra de
linha 2"""
print(quebra_de_linha2)
# quebra de
# linha 2

salto_de_linha = """
salto de linha

salto de linha"""
print(salto_de_linha)
# salto de linha
#
# salto de linha

outro_salto = """
string
"""
"======================================================================================================================"



# 18kek2a5g1aedpsvaevflvi2q7nbxaf672uz8yyys9ec1bm2nwetjd1n1stkauqte75o5c16uqf4etjvqb2qh9ubph3sq1mgnms9
# Remoção de todos os arquivos em uma pasta [ arquivos & pastas ]
# Não funciona caso dentre os arquivos, há pasta(s) que esteja(m) com arquivo(s) interno(s)
# É preciso adentrar toda(s) essa(s) pasta(s) e deletar o(s) arquivo(s) e pasta(s) aninhada(s) em sua totalidade
# Porém, não há conhecimento suficiente de minha parte para executar tal procedimento
"======================================================================================================================"
from os import scandir, remove, rmdir

# 1 - var = casting(método(caminho até a pasta))
# 2 - [ scandir() ], disponibiliza os arquivos/pastas do caminho especificado como argumento nos seus parâmetros
# 3 - [ scandir() ] também disponibiliza métodos secundários que auxiliam na chacagem
# 4 - Para este procedimento, o método secundário essencial é o [ .is_file() ]
# 5 - [ .is_file() ] filtra os dados por tipo, ou seja, sendo arquivo, retorna-se [ True ], e sendo pasta, [ False ]
var = tuple(scandir('C:\\Users\\Lucas\\Desktop\\pasta'))
print(var)

# Formas de verificação [ não são mandatórios ]
verificar_se_arquivo_ou_pasta_simples = [each_data.is_file() for each_data in var]
print(verificar_se_arquivo_ou_pasta_simples)

verificar_se_arquivo_ou_pasta_extenso = [(each_data, each_data.is_file()) for each_data in var]
print(verificar_se_arquivo_ou_pasta_extenso)

# Separação de arquivos e pastas para deletação eficiente (livre de erro)
# 1 - Cria-se um list comprehension com condicionais para deletar separadamente arquivos e pastas
# 2 - Não se pode deletar todos de uma vez, pois nem todos podem ser do mesmo tipo
# 3 - Para deletar arquivos, usa-se o método [ remove() ]
# 4 - Para deletar pastas, usa-se o método [ rmdir() ]
# 5 - No list comprehension, separa-se o procedimento para deletar arquivos na condição if
# 6 - No list comprehension, separa-se o procedimento para deletar pastas na condição else
remover_arquivos = [remove(each_data) if each_data.is_file() else rmdir(each_data) for each_data in var]
print(remover_arquivos)
"======================================================================================================================"



# ttx61kfiogsz59kltrhsy2tk1kq4pdijs5etzhkl999bwbuepwwnzixtsr24hcj1h8ses2dhgyuuoqnmkvok7fwucuayn39e9siw
# Resto de divisão pythônica de dados flutuantes [ 3 maneiras de arredondamento bruto ] [ != de round() ]
"======================================================================================================================"
contexto = ('print', 'valor da variável', 'variável própria', 'variável nova')
contexto2 = ('pós-variável',)

var = 2020 // 7
print(var)          # 288 [ método // ]

var2 = 2020 / 7
print(int(var2))    # 288 [ método cast int ]

from math import trunc  # método prefixado
var3 = 2020 / 7
var4 = trunc(var3)
print(var4)         # 288 [ método trunc ]

"Contexto pós-variável"
var = 8
var //= 3
print(var)
"======================================================================================================================"



# xome3er8hss2jtlof3etsxehmvwh8pz77nsxr6dp5dgt1ds3cju7kmfdjcvjzt62a79eyec7opiu9uxerzorzwccxj3bktra1fj3
# Set comprehension
# [ iteração em linha ]
"======================================================================================================================"
dicio = {1: True, 2: 'False', 3: round(7.7)}
lista = [1, 2, 3, 4, 'cinco']

conj = {dados for dados in lista}
print(conj)   # {1, 2, 3, 4, 'cinco'}

conj2 = {dados for dados in dicio}
print(conj2)  # {1, 2, 3}

conj3 = {dados for dados in dicio.values()}
print(conj3)  # {8, True, 'False'}

conj4 = {dados for dados in dicio.items()}
print(conj4)  # {(3, 8), (1, True), (2, 'False')}
"======================================================================================================================"



# 6clz9swcfh87hlw4qvkdks8h7l4gisphu9n2pnmhhqsosr9xre4glnk4y7nnf4gal47tnm14jsbya45wbc2rlvow6crqk8dbtxr1
# Shallow copy
# [ herança de dados ] [ gerador de elo ]
"======================================================================================================================"
lista = ['...', 'vazio', '']
tupla = lista  # [ Herança de dados ] [ gerador de elo ]
print(tupla)   # ['...', 'vazio', '']
tupla.clear()

print(tupla)   # []
print(lista)   # []

conj = {0, 0.0, '0', (0,)}
lista = conj  # [ Herança de dados ] [ gerador de elo ]
print(lista)  # {0, (0,), '0'}
lista.add('string')
print(lista)  # {0, 'string', (0,), '0'}
print(conj)   # {0, 'string', (0,), '0'} -> [ Alteração global ]
"======================================================================================================================"



# 35zyzsfzcfl3npdngl4x5dvvqrmj8f5zquk1ga7x248nxwxe2tgbcrqn7dqutb9fat9lszy7gq91a64tyjthwsb3ahq1zlvxfm1h
# Acesso de índice por variável [ alternativo ] [ utilidade maior em classe conjunto ]
# [ herança de dados ] [ equivalência de dados mandatória ]
"======================================================================================================================"
contexto = ['valor da variável']

lista = [False, 1j, {2}, {3: 3}, 4.0, 5, [6], range(7, 8), None, '9', (10,)]
a, b, c, d, e, f, g, h, i, j, k = lista

print(f)  # 5
"======================================================================================================================"



# lk35igu1ywf8co2udja264dhe4o5mvyl3pp89zph7ci8q1dug7269vhlxn6cylhfiivxr33nkwdrd59yxu7vi11v7m22js6qxkjl
# Slice
# [ slice regular ] [ 1 à 3 argumentos ] [ ínício:fim:salto ] [ tolerância: lista // range // string // tupla ]
"======================================================================================================================"
contexto = ['print', 'valor da variável', 'variável própria', 'variável nova']

conj = {'Lucas', 'Farias', 'Santos', 'de', 'Sousa'}
dicio = {'Lucas': None, 'Farias': None, 'Santos': None, 'de': None, 'Sousa': None}
lista = ['Lucas', 'Farias', 'Santos', 'de', 'Sousa']
string = 'Lucas Farias Santos de Sousa'
tupla = 'Lucas', 'Farias', 'Santos', 'de', 'Sousa'

print('slice de string\n', string[1:])     # ucas Farias Santos de Sousa
print('slice de tupla\n', tupla[:4])       # ('Lucas', 'Farias', 'Santos', 'de')
print('slice de lista\n', lista[::2])      # ['Lucas', 'Santos', 'Sousa']
print('slice de string\n', string[1:4])    # uca
print('slice de tupla\n', tupla[0::4])     # ('Lucas', 'Sousa')
print('slice de lista\n', lista[:3:2])     # ['Lucas', 'Santos']
print('slice de string\n', string[0:5:3])  # La
print('slice de tupla\n', tupla[::-1])     # ('Sousa', 'de', 'Santos', 'Farias', 'Lucas')

# print(conj[0:5])     # TypeError: 'set' object is not subscriptable
# print(dicio[1:3:2])  # TypeError: unhashable type: 'slice'
"======================================================================================================================"



# ilurzos7mjxemjteg4difdw5zxseo58klydyn44cx7jhxtdtjd1b6sgx4ngcz2kxfrabvig7xkqpejsuumpgjciobe8zztf24w4l
# Slice de inversão
# [ slice invertido ] [ ordenação da direita para esquerda ] [ intolerância: conjunto / dicio ]
"======================================================================================================================"
contexto = ('print', 'valor da variável', 'variável própria', 'variável nova')

conj = {True, 0, ''}
print(conj[::-1])    # TypeError: 'set' object is not subscriptable

dicio = {'nome': 'Lucas', 'ano': 2020}
print(dicio[::-1])   # TypeError: unhashable type: 'slice'

lista = [True, 0, '']
lista2 = lista[::-1]
print(lista2)        # ['', 0, True]

range_ = tuple(range(1, 6))[::-1]
print(range_)        # (5, 4, 3, 2, 1)

string = 'string'
print(string[::-1])  # gnirts

tupla = ('a', 'b', 'c', 'd')
tupla = tupla[::-1]
print(tupla)         # ('d', 'c', 'b', 'a')
"======================================================================================================================"



# 9yn3bpj4ltbrs8bm8gyd2jbuflai1i28pr6zz6nns7myldluhcmroubfp6ldj2lzayuuuuqw8ma9zpipc2w6s1865nug648vmu33
# Trabalhando com data: modificando mês para padrão brasileiro [ modelando data ]
"======================================================================================================================"
from datetime import datetime
# from textblob import TextBlob

data = datetime.now()


def tradutor_meses(date):
    if date.month == 1:
        return "{} de janeiro de {}".format(date.day, date.year)
    elif date.month == 2:
        return "{} de fevereiro de {}".format(date.day, date.year)
    elif date.month == 3:
        return "{} de março de {}".format(date.day, date.year)
    elif date.month == 4:
        return "{} de abril de {}".format(date.day, date.year)
    elif date.month == 5:
        return "{} de maio de {}".format(date.day, date.year)
    elif date.month == 6:
        return "{} de junho de {}".format(date.day, date.year)
    elif date.month == 7:
        return "{} de julho de {}".format(date.day, date.year)
    elif date.month == 8:
        return "{} de agosto de {}".format(date.day, date.year)
    elif date.month == 9:
        return "{} de setembro de {}".format(date.day, date.year)
    elif date.month == 10:
        return "{} de outubro de {}".format(date.day, date.year)
    elif date.month == 11:
        return "{} de novembro de {}".format(date.day, date.year)
    elif date.month == 12:
        return "{} de dezembro de {}".format(date.day, date.year)

print(tradutor_meses(data))

"Forma mais pythônica [ ineficiente pela demora de processamento ]"
# from textblob import TextBlob
# mes = datetime.now()
#
#
# def tradutor(var):
#     return '{} de {} de {}'.format(var.day, TextBlob(var.strftime('%B')).translate(to='pt-br'), var.year)
#
# print(tradutor(mes))
"======================================================================================================================"



# 6fmbha5q1snhujaji3sslrdwmywyp397ssm59uoyk3od7nt898pk6st7czrojt9qt78fgbe8qos7x478nqr9qjidbs7ytpq4jjti
# Formas de usar o método strftime e não usar strftime
"======================================================================================================================"
from datetime import datetime

# Data no formato americano (forma 1)
data_formato_americano = str(datetime.now()).split()[0]
print(data_formato_americano)                                                                              # 2020-07-06

# Data no formato americano (forma 2)
data_formato_americano2 = datetime.now().strftime('%Y/%m/%d')
print(data_formato_americano2)                                                                             # 2020/07/06

# Data no formato brasileiro
data_formato_brasileiro = datetime.now().strftime('%d/%m/%Y')
print(data_formato_brasileiro)                                                                             # 12/05/2020

# Outras dicas rápidas
# %Y = aaaa     # %y = aa                                          (formatos de ano completo e abreviado)
# %m por %B = substituição do nº do mês pelo nome do mês           (Inglês)
# %m por %b = substituição do nº do mês pelo nome do mês abreviado (Inglês)
"======================================================================================================================"



# anwrrdspgl5jknt1uamdmjg6rcg7i66ylxwhktpp8x5ckwy933l48hos1wp4rerbpk8155o46xg991i3y345olcahqxj2n1jydis
# Trabalhando com tempo: uso de [ datetime() ] para descobrir tempo de vida, dias remanescentes para aniversário
"======================================================================================================================"
from datetime import datetime

"Cálculo de dias de vida [ pt-br ]"
###################################
data_agora = datetime.now()
meu_nascimento = datetime(year=1992, month=7, day=16)
dias_de_vida = '{} dias'.format(str((data_agora - meu_nascimento)).split()[0])
print(dias_de_vida)
###################################

"Cálculo de dias de vida [ us ]"
################################
data_today = datetime.now()
my_birth = datetime(year=1992, month=7, day=16)
life_days = '{} days'.format(str((data_today - my_birth)).split()[0])
print(life_days)
################################

"Cálculo para fim do ano"
#########################
date_today = datetime.now()
new_year = datetime(date_today.year + 1, 1, 1, 0, 0, 0)
end_year = new_year - date_today
print(end_year)
#########################

"Cálculo para dias remanescentes para aniversário caso não tenha acontecido"
############################################################################
date_today = datetime.now()                    # get today's date
my_birthday_this_year = datetime(2020, 7, 16)   # customize my birthday for this year [ it hasn't occured ]

if my_birthday_this_year > date_today:                           # if my birthday this year is ahead of today's date
    remaining_days_case1 = (my_birthday_this_year - date_today)  # perform the following math
    remaining_days_case1 = str(remaining_days_case1).split('.')
    remaining_days_case1.pop()
    remaining_days_case1 = ' '.join(remaining_days_case1)
    print(remaining_days_case1)

"Problemas, não sei como fazer"
# else:                                                           # if my birthday this year has occured already
#     trespassed_days = my_birthday_this_year - date_today        # remaining days becomes trespassed days [ same math ]
#     new_year = datetime(date_today.year + 1, 1, 1)              # customize the new year date
#     new_year_countdown = new_year - date_today                  # get how many days there are to new year
#     remaining_days_case2 = trespassed_days + new_year_countdown
#     print(trespassed_days)
#     print(new_year_countdown)
#     print(remaining_days_case2)
###################################################################
"======================================================================================================================"



# 1u87ywdmyedamrigr3m2equphcf3np4cvuwo7fnfk48zxfmyjplen1ky4tskvr8hhqm9znufyg19n1wlrwtabdc7im64wlqsxuv3
# Trabalhando com tempo: uso de [ weekday() ] implícito com método [ datetime() ] em um pequeno algoritmo
"======================================================================================================================"
from datetime import datetime

nascimento = input('Informe sua data de nascimento\nUse o seguinte formato: dd/mm/aaaa\n-> ')
nascimento = nascimento.split('/')
nascimento = datetime(year=int(nascimento[2]), month=int(nascimento[1]), day=int(nascimento[0]))

if nascimento.weekday() == 0:
    print('Seu nascimento foi numa Segunda-feira')

elif nascimento.weekday() == 1:
    print('Seu nascimento foi numa Terça-feira')

elif nascimento.weekday() == 2:
    print('Seu nascimento foi numa Quarta-feira')

elif nascimento.weekday() == 3:
    print('Seu nascimento foi numa Quinta-feira')

elif nascimento.weekday() == 4:
    print('Seu nascimento foi numa Sexta-feira')

elif nascimento.weekday() == 5:
    print('Seu nascimento foi numa Sábado')

elif nascimento.weekday() == 6:
    print('Seu nascimento foi num Domingo')
"======================================================================================================================"



# sn4y9n91vrywz9p9gzjqb8gk2tku4wi11zdmv1movu95l6a4yso39vgssfpxndgvr417plqfskq34zbfdy91vyg4bcybsbbsmbqr
# Leitura e manipulação de arquivos de textos de forma alternativa
"======================================================================================================================"
from os import chdir

chdir('c:\\users\\lucas\\desktop')
with open('seek.txt', 'r') as doc:
    # FORMA DE LEITURA COMPLETA
    leitura = str(doc.read()).split('\n')
    print(leitura[0])  # Eu sou doido de pedra
    print(leitura[1])  # Eu não como fígado
    print(leitura[2])  # Minha vida é uma merda

with open('seek.txt', 'r') as doc:
    # FORMA DE LEITURA ESPECIFICADA
    leitura = doc.read().split('\n')
    print(leitura[0][16:])  # pedra
    print(leitura[1][12:])  # fígado
    print(leitura[2][17:])  # merda
"======================================================================================================================"



# tup1q8r4x2ciyxsmxdareavjn9ngvbd4u12l6zkhx3fg87wo8tecxe7allo5n2hujj9m81k4mgjedyp9t7n4vt3x9pa4owfzaatt
# Tratamento de tempo de acordo com os períodos do dia com [ condicionais ] & [ operadores relacionais ]
"======================================================================================================================"
from datetime import datetime

tempo = datetime.today()

"Criação das condições de forma externa"
if 17 < tempo.hour <= 23:
    print('Boa noite!')
elif 12 <= tempo.hour <= 17:
    print('Boa tarde!')
else:
    print('Bom dia!')

"Criação de condições em comprehension (algumas regras)"
# Regra 1 - É recomendável que crie-se uma variável fora para interagir com as condições dentro de uma lista
# Regra 2 - Recomenda-se que a variável externa esteja na mesma ordem de acontecimento das condições
"No contexto desse exemplo, seria dizer que:"
# saudar[0] é a condição de chances[0]
# saudar[1] é a condição de chances[1]
# saudar[2] é a condição de chances[2]

saudar = ('Boa noite!', 'Boa tarde!', 'Bom dia!')

chances = [
    [True if 17 < tempo.hour <= 23 else None],
    [True if 12 <= tempo.hour <= 17 else None],
    [True if tempo.hour < 12 else None]
]

indice_alvo = chances.index([True])
print(saudar[indice_alvo])
"======================================================================================================================"



# lgz672619cfrtlp3fdxj56vmzkwd3f3uemna63dppcwch13u1bqq7x13t1jrd6cms11vyeybj7bi9dg3mdte6yjuzamljyv9i121
# variável de dados complexos
# [ exemplificação de dados complexos em coleção ]
"======================================================================================================================"
from random import randint

lista = [[dados for dados in list(range(1, 501)) if not dados % 100],
         list(range(1, 8)),
         sum([7 ** 7, - 7]),
         (randint(1, 100), randint(1, 1000), randint(1, 10000)),
         'Meu nome é {}'.format('_'.join('Lucas'[::-1]))]
print(lista)  # [[100, 200, 300, 400], [1, 2, 3, 4, 5, 6, 7], 823536, (52, 249, 9390), 'Meu nome é s_a_c_u_L']
"======================================================================================================================"



# b3hi6vly7tvrvl5ip2o2x6c1yahf5tzvh5a5ge3fb7j35uof834hvutmhkaruu7zskue312o2cj2x1mva3tykzdpzmub7kod5moc
# Criação de arquivos textuais, de forma reciclável e concatenada
"======================================================================================================================"
from os import chdir

chdir('c:\\users\\lucas\\desktop\\docs_container')

# CRIAÇÃO DE UM ARQUIVO RECICLÁVEL (atualização de conteúdo = substituição do conteúdo novo pelo antigo)
with open('arquivo_criado_reciclavel.txt', 'w') as doc:
    doc.write('a')

# CRIAÇÃO DE UM ARQUIVO ACUMULATIVO (atualização de conteúdo = concatenação do conteúdo antigo com o novo)
with open('arquivo_criado.txt', 'a') as doc:
    doc.write('pirotécnico')
"======================================================================================================================"
