

from os import chdir

def infos():
    """
    Objetivo:
        criar um módulo de texto com inserção de dado único, ou seja, sobreposição, caso algo novo seja escrito

    Objetivo 2:
        criar um módulo de texto com inserção de dados múltiplos, ou seja, acumulação, caso algo novo seja escrito

    Objetivo 3:
        ler dados de um módulo de texto criado previamente à leitura
    """

chdir('/home/lucas/Desktop/')  # mudando a rota para criar módulo na área de trabalho

# Forma mais antiga de criar módulo, com sobreposição de dados 'w'
def ex() -> None:
    arquivo = open('testar.txt', 'w')      # a criação do módulo acontece aqui, apesar da sintaxe dizer "abrir"
    arquivo.write('Bem-vindo ao Python')   # mesclar a variável do módulo com o método .write(), para escrever textos
    arquivo.close()                        # ao terminar a escrita, deve-se fechar o módulo, através do método .close()
    arquivo = open('testar.txt', 'w')      # numa segunda chamada, o arquivo não é recriado, mas, acessado novamente
    arquivo.write('Bem-vindo ao Python2')  # porém, o parâmetro 2: 'w', impede que qualquer novo texto seja inserido
    arquivo.close()                        # ao final, é mandatório fechar o módulo, na forma mais antiga

# Forma mais antiga de criar módulo, com acumulação de dados 'a'
def ex2() -> None:
    arquivo = open('testar2.txt', 'a')      # como o segundo parâmetro é 'a', novos textos podem ser inseridos
    arquivo.write('Bem-vindo ao Python\n')  # texto 1
    arquivo.close()
    arquivo = open('testar2.txt', 'a')      # segunda chamada, para adicionar novos dados
    arquivo.write('Bem-vindo ao Python2')   # texto 2
    arquivo.close()

# Forma mais antiga de ler um módulo 'r'
def ler_ex2() -> None:
    arquivo = open('testar2.txt', 'r')  # a declaração de leitura acontece aqui, pelo 'r'
    print(ler := arquivo.read())        # a declaração é mesclada ao método .read(), para ler o(s) texto(s)
    arquivo.close()

ex2(), ler_ex2()

# Forma mais atual de criar módulo, com sobreposição de dados 'w'
def ex3() -> None:
    # A forma mais nova, cria uma variável interna, ao invés de externa
    with open('testar3.txt', 'w') as txt:
        txt.write('Bem-vindo ao Python - exemplo 3')
    with open('testar3.txt', 'w') as txt:
        txt.write('Bem-vindo ao Python - exemplo 3.1')
        # A forma mais nova dispensa o método de fechar um módulo, pois ela faz isso automaticamente

# Forma mais atual de criar módulo, com acumulação de dados 'a'
def ex4() -> None:
    with open('testar4.txt', 'a') as txt:
        txt.write('Bem-vindo ao Python - exemplo 4\n')
    with open('testar4.txt', 'a') as txt:
        txt.write('\nBem-vindo ao Python - exemplo 4.1')

# Forma mais atual de ler um módulo 'r'
def ler_ex4() -> None:
    with open('testar4.txt', 'r') as txt:
        print(ler := txt.read())

ex4(), ler_ex4()
