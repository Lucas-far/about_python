

"""
Objetivo:
    - Declarar variáveis da forma mais específica possível

Observação:
    - A declaração é apenas uma referência, se os dados apresentam não forem do tipo especificado, não haverá erro
"""

from typing import Dict, List, Set, Tuple

# Tipo que pode especificar vários tipos: Tupla
tupla_1: Tuple[bool, list, complex] = (True, [], 1j)
print(tupla_1)

# Tipo que pode especificar dois tipos: Dicionário
dicionario_1: Dict[str, str] = {'nome': 'Jânio', 'idade': '62', 'atleta': 'False'}
dicionario_2: Dict[str, bool] = {'É ser humano?': False, 'É selvagem?': True}
print(dicionario_1)
print(dicionario_2)

# Tipos que podem especificar um tipo: Conjunto e Lista
conjunto_1: Set[int] = {1, 2, 3}
lista_1: List[bool] = [True, False]
print(conjunto_1)
print(lista_1)
