

"""
Objetivo:
    operador Python que permite declaração e retorno de uma expressão ao mesmo tempo
"""

def fonte():
    """
    Curso  # Programação em Python do básico ao avançado
    Seção  # Seção 24:Novidades do Python 3.8
    Aula   # 167. O operador Walrus
    """

# Exemplos com uma forma antiga (sem walrus)
l = [each_data ** 2 for each_data in range(1, 6)]
s = 'string'
cj = {'senha': 'habab0.701'}
print([1], l, [2], s, [3], cj)

# Exemplos com a forma mais atual (com walrus)
print([1], l2 := [each_data ** 2 for each_data in range(1, 6)])
print([2], s2 := 'string')
print([3], cj2 := {'senha': 'habab.701'})


# Exemplo do operador Walrus em um algoritmo pequeno
def get_value_input_type():
    """To treat improper data while a proper integer number is not being provided."""

    input_text: str = \
        f"""
        ========== Qual adjetivo abaixo, melhor representa você? ==========
        1. Clique na seta abaixo
        2. Escolhe um dos valores
        3. Aperte ENTER\n
        ========== OPÇÕES ==========
        1. Matuto abestalhado 2. Anti-social 3. Atentado 4. Perturbado 5. Retardado 6. Imbecil
        -> """

    unexpected_int: str = \
        """
        \033[1:31m========== Erro ==========\033[m
        Valor válidos: entre 1 até 6
        """

    unexpected_class: str = \
        """
        \033[1:31m========== Erro ==========\033[m
        Tipo de valor aceitável: inteiro
        Valores válidos: entre 1 até 6
        """

    adjectives: tuple = ('', 'Matuto abestalhado', 'Anti-social', 'Atentado', 'Perturbado', 'Retardado', 'Imbecil')

    while True:
        try:
            while (input_option := int(input(input_text))) < 1 or input_option > 6:
                print(unexpected_int)
                get_value_input_type()
            else:
                print(f'\nVocê é [{"".join(adjectives[input_option])}]')
                break
        except ValueError:
            print(unexpected_class)
        except KeyboardInterrupt:
            print('Algoritmo interrompido!')

get_value_input_type()
