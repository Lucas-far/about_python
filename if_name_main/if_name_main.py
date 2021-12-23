

"""
Objetivo:
    impedir que usos de objetos (variáveis ou funções) de um módulo herança, reflitam em um módulo herdeiro
"""

# Cria-se um módulo, onde seus dados serão herdados
"raiz / new / python file / teste.py"

# O erro implícito começa, pelo fato de o módulo possuir testes no escopo global dele
def dados():
    """
    file = 'testar.py'

    def somar(*args):
        count = 0
        for each_number in args:
            count += each_number
        print(count)

    somar(-200, -27)
    print('1.' + file)
    """

# Os testes são:
"somar(-200, -27)"
"print('1.' + file)"

# Cria-se um segundo módulo, onde seus dados serão herdeiros
"raiz / new / python file / teste2.py"

# O segundo módulo importa o primeiro, para poder usar seus dados
def dados2():
    """
    import testar

    testar.somar(200, 27)
    print(testar.file)
    """

# Na impressão do segundo módulo, não gera-se um erro, mas geram-se dados excedentes. Qual a razão disso?
"No primeiro módulo, que é o passador da herança, há testes dos dados no escopo global"

# Qual o problema de haver testes no escopo global?
"Se esse módulo for importado para outro, quando o segundo módulo usar os dados, será mostrado ambos os testes"

# Como assim, ambos testes?
"Os testes feitos no módulo de herança, e no herdeiro"

# Como resolve-se isso?
"No módulo de herança, criar uma condição: [ if __name__ == '__main__': ] e então inserir os testes nesse escopo"

def dados_add_if():
    """
    file = 'testar.py'

    def somar(*args):
        count = 0
        for each_number in args:
            count += each_number
        print(count)

    if __name__ == '__main__':
        somar(-200, -27)
        print('1.' + file)
    """

# Essa condição precisa ser criada no módulo herdeiro, também?
"Não, apenas no de herança, e após isso, os dados podem ser usados, sem gerar resultados excedentes"
