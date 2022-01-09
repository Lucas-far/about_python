

from pandas import read_csv

# Só está sendo passado o nome e o formato pelo fato deste arquivo e o arquivo csv estarem no mesmo diretório
file_csv = read_csv('pokemon_data.csv')
print(file_csv)

# Filtra quantos cabecalhos serão mostrados por vez (de cima para baixo)
print(file_csv.head(3))

# Filtra quantos cabeçalhos serão mostrados por vez (de baixo para cima)
print(file_csv.tail(3))
