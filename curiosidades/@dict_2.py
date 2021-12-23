

"""
Curiosidade? Classe dicionário com dicionários aninhados e formas de chamar
"""

dicio = {
    'chave_mãe': {
        'chave_filha1': 'valor1',
        'chave_filha2': 'valor2'
        }
    }

print(dicio['chave_mãe'])
print(dicio['chave_mãe']['chave_filha1'])
