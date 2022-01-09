

from pandas import Series

# OBJETIVO: Localizar um dado Series pelo valor do seu índice (par 2)
pessoas = 'Ana Ena Ina Ona Una'.split(' ')  # 5 índices
idades = [*range(16, 21)]                   # 5 índices
pessoas_idades = Series(data=pessoas, index=idades)

# 20 não é o número do índice como em Python, é o valor desse índice
pessoa_5 = pessoas_idades.loc[20]

print([1], pessoas_idades)
print([2], pessoa_5)
