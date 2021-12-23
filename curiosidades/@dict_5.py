

"""
Curiosidade? troca de dados entre dicionários
"""

dicionario = {'a': False, 'b': None, 'c': True}
print([1], dicionario)
dicionario['a'] = dicionario['c']  # Aqui acontece a troca, a chave 'a' está tendo tendo seu valor igualado à chave 'c'
print([2], dicionario)             # Note a mudança em relação da chave 'a' à impressão anterior da variável

# A troca de chaves pode ser multipla, sendo os dados outras chaves ou até mesmo valores literais
dicionario['b'], dicionario['c'] = dicionario['c'], dicionario['a']
print([3], dicionario)
