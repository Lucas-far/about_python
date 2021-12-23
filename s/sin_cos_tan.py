

from math import cos, radians, sin, tan


def objetivo():
    """ Fazer conversões de seno, cosseno, tangente """


angulo = 45
print([1], seno := sin(radians(angulo)))
print([1.1], round(seno, 2))
print([1.2], f'{seno:.2f}')

print([2], cosseno := cos(radians(angulo)))
print([2.1], round(cosseno, 2))
print([2.2], f'{cosseno:.2f}')

print([3], tangente := tan(radians(angulo)))
print([3.1], round(tangente, 2))
print([3.2], f'{tangente:.2f}')
