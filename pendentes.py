

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
