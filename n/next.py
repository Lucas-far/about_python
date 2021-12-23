

def objetivo():
    """
    Percorrer dados, similarmente ao loop for, só que não sendo automático (obsoleto)
    - Pode ser útil para filtrar dados pequenos
    - Para poder usar [ next() ] o dado precisa ser iterável e receber [ iter() ]
    """


nome = 'Lucas'
nome = iter(nome)

print(next(nome))
next(nome)  # Dados chamados sem [ print() ] ficam omitidos
print(next(nome))
next(nome)
print(next(nome))
