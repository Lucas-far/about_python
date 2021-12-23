

"""
Objetivo
    forma alternativa de usar a classe lista

Observação
    A classe deque é a classe lista, só que além de ter os métodos de lista, têm os seus próprios
"""

from collections import deque

# Instanciação de um deque
print(dq := deque([]))

# Por ser um upgrade da classe lista, deque contêm as bibliotecas de ambos
dq.append(True)          # método lista e deque
dq.appendleft(False)     # método deque
dq.extend(range(0, 1))      # método lista
dq.extendleft(range(1, 4))  # método lista e deque

print(dq)
