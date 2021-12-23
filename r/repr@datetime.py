

from datetime import datetime


def objetivo():
    """
    Converter um objeto [ datetime ] para [ str ]
    Relacionados: ver módulo [ !r.py ]
    """


print([1], hoje := datetime.now())
print([2], repr(hoje))

# O método [ repr ] converte um objeto [ datetime ] para [ str ], tornando a filtragem de dados mais fácil
print([3], hoje_lista := repr(hoje).replace('datetime', '')
                                   .replace('.', '')
                                   .replace('(', '')
                                   .replace(')', '')
                                   .replace(' ', '')
                                   .split(','))
