

"""
Objetivo:
    -

Observação:
    -
"""


def informar_data(ordem):

    from datetime import datetime

    day, month, year = '%d', '%m', '%Y'  # Uso aqui

    ordens = (
        'dia mês ano', 'dia ano mês', 'mês dia ano', 'mês ano dia', 'ano dia mês', 'ano mês dia',
    )

    msg_error = 'ERRO: Por favor, basei-se nos exemplos abaixo\n----- EXEMPLOS -----\n1. dia mês ano\n2. ano mês dia'

    now_ = datetime.today()

    # Uso aqui
    conditions = {
        ordens[0]: now_.strftime(f'{day}/{month}/{year}'),
        ordens[1]: now_.strftime(f'{day}/{year}/{month}'),
        ordens[2]: now_.strftime(f'{month}/{day}/{year}'),
        ordens[3]: now_.strftime(f'{month}/{year}/{day}'),
        ordens[4]: now_.strftime(f'{year}/{day}/{month}'),
        ordens[5]: now_.strftime(f'{year}/{month}/{day}'),
    }

    if ordem in ordens:
        for key in conditions:
            if key == ordem:
                return conditions[key]
    return msg_error


if __name__ == '__main__':
    caixa = (
        'dia mês ano', 'dia ano mês', 'mês dia ano', 'mês ano dia', 'ano dia mês', 'ano mês dia',
    )

    print(informar_data(ordem='dia-mês-ano'))
    print(informar_data(ordem=caixa[0]))
    print(informar_data(ordem=caixa[1]))
    print(informar_data(ordem=caixa[2]))
    print(informar_data(ordem=caixa[3]))
    print(informar_data(ordem=caixa[4]))
    print(informar_data(ordem=caixa[5]))
