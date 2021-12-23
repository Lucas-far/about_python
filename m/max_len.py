

"""
Ojetivo:
        parâmetro para determinar a quantidade máxima de índices que uma classe deque pode possuir

Detalhe:
        1 - o uso desse parâmetro resulta no remoção de índices, caso o número de dados exceda
        1 - porém, existe uma lógica:

            1.1 - appendleft/extendleft =======> deleta-se índices da direita
            1.1 - append/extend         =======> deleta-se índices da esquerda
"""

from collections import deque

dq = deque(range(1, 11), maxlen=10)
print([1], dq)
dq.appendleft(66)
print([2], dq)
dq.extendleft(range(-99, -98))
print([3], dq)
dq.append(9)
print([4], dq)
dq.extend(range(10, 11))
print([5], dq)
