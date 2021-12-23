

"""
Objetivo:
    ...
"""

from importlib import metadata

def fonte():
    """

    """

# print([1], metadata.metadata("pip"))  # mostrar versão do metadata e um relatório
print([2], metadados := list(metadata.metadata("pip")))
print([3], len(metadata.files("pip")))              # 753
print([4], metadata.requires('pip'))                # pip install pip
print([5], metadata.requires('django'))             # pip install django
print([6], metadata.requires('django-bootstrap4'))  # pip install django-bootstrap4

# for x in metadados:
#     print('\033[1:32m' + 'metadata.metadata("pip")["' + f'{x}' + '"]' + '\033[m', metadata.metadata("pip")[f"{x}"])
#
# print(f'{tuple(enumerate([metadata.metadata("pip")[f"{x}"] for x in metadados]))}')
