

# tozzcv6b1i1pzd6pn89qk5uwmtzsb57ubvs75s6ha49a7p82zhd92x5fv8ufsvogrj4umz414r3zlmywi5ypf6x9go2e6x84m7jy
# reduce
# [ importação mandatória ] [ dependente de lambda com 2 parâmetros ] [ 2 args = lambda de 2 par, iterador ]
# [ iterador de dados = loof for piorado ]
"======================================================================================================================"
# contexto = ['print', 'valor da variável', 'variável própria', 'variável nova']

# var = reduce(lambda x, y: x + '\n' + y, {'nome', 'sobrenome', 'idade', 'nacionalidade', 'língua', 'cor de pele'})
# print(var)
# cor de pele
# idade
# nacionalidade
# língua
# nome
# sobrenome

# var2 = reduce(lambda x, y: x.upper() + '\n' + y.upper(), {'nome', 'sobrenome', 'idade', 'nacionalidade'})
# print(var2)

# SOBRENOME
# NOME
# IDADE
# NACIONALIDADE
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
