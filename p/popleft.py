

"""
Objetivo:
    remover o primeiro índice de uma classe deque, mas não em uma lista
"""

from collections import deque

print([1], dq := deque([*range(1, 10)])), dq.popleft(), print([2], dq)

# Quando uma lista tenta usar um método de deque
print([2], l := ['l', 'i', 's', 't', 'a'])

""" l.popleft() """  # AttributeError: 'list' object has no attribute 'popleft'

# A solução contextual
l = deque(l)
l.popleft()
l = list(l)
print([3], l)
