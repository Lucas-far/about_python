

from typing import Literal, Union

def fazer_conta(v: Union[int, float], op: Literal['+', '-', '*', '/', '**', '|'], v2: Union[int, float]) -> None:
    invalid = '\n========== Erro ==========\nO operador fornecido é inválido:'
    invalid_ = '\n========== Erro ==========\nDivisão por zero é inválida'
    try:
        if op == '+' or op == '-' or op == '*' or op == '/' or op == '**':
            conditions = [
                [f'{v} + {v2} = {v + v2:.2f}' if op == '+' else None],
                [f'{v} - {v2} = {v - v2:.2f}' if op == '-' else None],
                [f'{v} x {v2} = {v * v2:.2f}' if op == '*' else None],
                [f'{v} / {v2} = {v / v2:.2f}' if op == '/' else None],
                [f'{v} ** {v2} = {v ** v2:.2f}' if op == '**' else None],
            ]
            while [None] in conditions:
                conditions.pop(conditions.index([None]))
            print("".join(conditions[0]))

        elif op == '|':
            conditions = [[f'raiz de {v} = {v ** 0.5:.2f}' if op == '|' else None]]
            print("".join(conditions[0]))

        else:
            print(f'{invalid} {op!r}')

    except ZeroDivisionError:
        print(invalid_)

fazer_conta(13, '*', 13.1)
