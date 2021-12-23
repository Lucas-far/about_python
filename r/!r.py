

"""
Objetivo:
    mostrar a impressão de um dado string de forma literal (envolto por '')

Observação:
    1. pode ser usado em outras classes iteráveis, se nelas há apenas dados string
    2. aparentemente, a sintaxe funciona somente no formato f'{}'
    3. não deve ser usado pra tentar mostrar um inteiro como string, pois não funciona
"""

def fonte():
    """
    Curso  # Programação em Python do básico ao avançado
    Seção  # Seção 24:Novidades do Python 3.8
    Aula   # 169. Tipos de dados mais precisos
    Tempo  # 10:05
    """

# @str

print([1], 'string')         # string sem sua marcação de aspas
print([2], f"{'string'!r}")  # string com sua marcação de aspas

# Exemplos mais complexos
print([3], ' '.join([str(each_data) for each_data in ['doido', 'maluco', 'biruta']]))
print([4], ' '.join([f"{str(each_data)!r}" for each_data in ['doido', 'maluco', 'biruta']]))
