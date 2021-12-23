

# Embaralhar dados em uma lista
from random import shuffle

var = list(range(1, 6))

while True:
    shuffle(var)
    print(var)
    print(input('APERTE ENTER'))
