

"""
Curiosidade? Criando um dicionário em forma de bdd
"""

# Por meio de uma chave matriz, obtemos acesso às chaves aninhadas e seus valores
dicio = {'Brasil': {'língua': 'português',
                    'estados': 27,
                    'clima': 'tropical'},

         'Outro': {'língua': None,
                   'estados': None,
                   'clima': None}
         }

print(dicio['Brasil'])
print(dicio['Brasil']['língua'])
print(dicio['Brasil']['estados'])
print(dicio['Brasil']['clima'])
print(dicio['Outro']['língua'])
print(dicio['Outro']['estados'])
print(dicio['Outro']['clima'])
