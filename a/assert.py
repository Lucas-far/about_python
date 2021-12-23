

def infos():
    """
    Objetivo:
         palavra reservada para testar códigos em funções e seus parâmetros

    Observação:
        1. o arg1 contêm operações relacionais que provêm que [ assert ] terá retorno = True
        2. o arg2 é uma string contendo uma mensagem de erro, para caso [ assert ] tenha retorno = False
        3. o arg2 é mostrado como [ AssertionError ]
    """

def mostrar_valores_positivos(a: int = 1, b: int = 1, c: int = 1):
    assert a > 0 and b > 0 and c > 0, 'Há valores negativos'
    print(a, b, c)

# Exemplo que ativa o segundo parâmetro do [ assert ]
"mostrar_valores_positivos(-1, 7, 10)"
"AssertionError: Há valores negativos"

def lanchonete(alimento: str) -> str:
    menu = {
            'sorvete de balnilha': 7.20,
            'suco de limão': 2.75,
            'bomba': 3.10,
            'caldo de cana': 5,
            'empada': 3.50,
            'churros de leite condensado': 4.20
    }

    for inteiro, cada_alimento in enumerate(menu.items()):
        print(inteiro, cada_alimento)

    assert alimento in menu, 'O cardápio não contém o alimento informado'

    return f'Você escolheu o alimento [ {alimento} ]'

# Exemplo que ativa o segundo parâmetro do [ assert ]
"print(lanchonete('arroz'))"
"AssertionError: O cardápio não contém o alimento informado"
