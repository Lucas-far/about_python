

def pendente_reduce():
    """
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
    """


def pendente_seek():
    """
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
    """


def pendente_testagem_poo():
    """
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
    """


def pendente_time_delta():
    """
    from datetime import datetime, timedelta

    data_compra = datetime.now()
    print(data_compra)       # 2020-05-12 12:07:01.388718
    prazo_vencimento = timedelta(days=30)
    print(prazo_vencimento)  # 30 days, 0:00:00
    data_vencimento = data_compra + prazo_vencimento
    print(data_vencimento)   # 2020-06-11 12:07:01.388718
    """


def pendente_wraps():
    """
    from functools import wraps


    def f(par):
        @wraps(par)  # Se @wraps(par) estivesse ausente, a consulta de documentação abaixo seria incorreta
        def f2(*args, **kwargs):
            ''' Função em Python v1 '''
            return par(*args, **kwargs)
        return f2


    @f
    def f3():
        ''' Função em Python v2 '''
        return


    print(f3.__doc__)
    # Consulta à documentação da função [ f3() ]...
    # Se @wraps(par) estivesse ausente...
    # A consulta ao documento da função [ f3() ] chamaria a documentação do decorador, função [ f() ]
    # Isso acontece, pois [ @f ] é um decorador da função [ f() ], e influencia a função [ f3() ]
    # Por causa dessa influência, a função [ f3() ] acessa a documentação de forma erônia
    # Mas a presença do @wraps(par) corrigi esse comportamento
    """


def pendente_yield():
    """
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
    """


def pendente_writer():
    """
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
    """
