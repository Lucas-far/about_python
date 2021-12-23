

from random import choice
from typing import Union


def fonte():
    """
    Curso || Programação em Python do básico ao avançado
    Seção || Seção 24:Novidades do Python 3.8
    Aula  || 169. Tipos de dados mais precisos
    Tempo || 16:30
    """


def objetivo():
    """ especificar mais de um tipo de classe que um parâmetro pode aceitar """


# Exemplo em parâmetros
def somar_ou_subtrair(operador: str,
                      valor: Union[int, float],
                      valor2: Union[int, float]) -> None:
    """"""

    msg_for_operator_plus = f'A soma de {valor} + {valor2} é igual a: {valor + valor2}'
    msg_for_operator_minus = f'A subtração de {valor} - {valor2} é igual a: {valor - valor2}'
    msg_for_wrong_operator = f'\n========== Erro ==========\nOperador inválido: {operador!r}'

    if operador == '+':
        print(msg_for_operator_plus)
    elif operador == '-':
        print(msg_for_operator_minus)
    else:
        print(msg_for_wrong_operator)


# Usar union com variados objetos requer condições mandatórias para definir em qual contexto cada tipo será usado
def meses(tipo_retorno: int) -> Union[str, list, tuple]:
    """
    :param tipo_retorno: choose from 1 to 3 (1 = returns string / 2 = returns list / 3 = returns tuple)
    :return:
    """

    i1 = 0
    meses_int = [*range(1, 13)]
    meses_lst = 'Janeiro Fevereiro Março Abril Maio Junho Julho Agosto Setembro Outubro Novembro Dezembro'.split()
    escolhido = choice(meses_lst)


    while True:
        if escolhido == meses_lst[i1] and tipo_retorno == 1:
            return f"O mês sorteado foi {escolhido}, que é representado pelo número {meses_int[i1]}"
        elif escolhido == meses_lst[i1] and tipo_retorno == 2:
            return list(f"O mês sorteado foi {escolhido}, que é representado pelo número {meses_int[i1]}")
        elif escolhido == meses_lst[i1] and tipo_retorno == 3:
            return tuple(f"O mês sorteado foi {escolhido}, que é representado pelo número {meses_int[i1]}")
        else:
            i1 += 1


if __name__ == '__main__':
    somar_ou_subtrair(operador='-', valor=1, valor2=1)
    somar_ou_subtrair(operador='+', valor=2, valor2=3)

    print(meses(tipo_retorno=1))
    print(meses(tipo_retorno=2))
    print(meses(tipo_retorno=3))
