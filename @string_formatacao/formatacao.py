

from typing import Union


def fonte():
    """
    Curso || Programação em Python do básico ao avançado
    Seção || Seção 24: Novidades do Python 3.8
    Aula  || 170. Debugger mais simples com f-strings
    """


def infos():
    """
    Objetivo
        alterar a exibição de dados numéricos em string
    """


def elevar(value: Union[int, float], potency: Union[int, float]) -> Union[int, float]:
    return value ** potency


if __name__ == '__main__':

    # ------------------------------------------- Usando objeto com fstring -------------------------------------------
    obj: Union[int, float] = elevar(value=2, potency=2.2)
    print([1], f'{obj}')      # Sem filtragem de casas decimais
    print([2], f'{obj:.1f}')  # Sintaxe p/ 1 casa decimal
    print([3], f'{obj:.2f}')  # Sintaxe p/ 2 casas decimais
    print([4], f'{obj:.3f}')  # Sintaxe p/ 3 casas decimais

    # ------------------------------------------------- Outras formas -------------------------------------------------
    print([5], '{:.4f}'.format(obj))
    print([6], f'{elevar(2, 2.2):.5f}')
    print([7], '{:.7f}'.format(elevar(2, 2.2)))

    # -------------------------------------------- Outro tipo de formatação --------------------------------------------
    nome = ' Python '
    nome_ = f" {nome:-^100} "
    print([8], nome_)
