

# Cria-se as variáveis em letra minúscula
vowels_lower = [
    'a', 'e', 'i', 'o', 'u'
    'ä', 'ë', 'ï', 'ö', 'ü',
    'à', 'è', 'ì', 'ò', 'ù',
    'á', 'é', 'í', 'ó', 'ú',
    'â', 'ê', 'î', 'ô', 'û',
    'ã', 'ẽ', 'ĩ', 'õ', 'ũ'
]

# Não precisa criar manualmente as versões maiúsculas, itera-se sob as minúsculas, convertendo-as para maiúsculas
vowels_upper = [each_data.upper() for each_data in vowels_lower]

# Inserem as duas numa variável só
vowels_all = [*vowels_lower, *vowels_upper]
print(vowels_all)

# Deleta-se as variáveis anteriores
del vowels_lower
del vowels_upper

# Para provar que, mesmo deletando as variáveis matriz, a var herdeira continua com os valores
print(vowels_all)
