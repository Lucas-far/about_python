

"""
Objetivo:
    mostrar que o operador condicional "or" possui uma sintaxe específica para uso múltiplo

Observação:
    1. a variável ou literal comparado deve ser repetida em todas os usos do "or"
    2. usar apenas um "or" e comparar com os dados em tupla, não funciona
    3. em caso das condições ocuparem mais de uma linha, usar: \
       na linha abaixo
"""

# condição de uma linha
op = 'b'
if op == 'a' or op == 'e' or op == 'i' or op == 'o':
    print('Sim')
else:
    print('Não')

# condição em linhas múltiplas
op2 = 'b'
if op2 == 'b' or op2 == 'c' or op2 == 'd' or op2 == 'f' or op2 == 'g' or op2 == 'h' or op2 == 'j' or op2 == 'k' \
 or op2 == 'l' or op2 == 'm' or op2 == 'n' or op2 == 'p' or op2 == 'q' or op2 == 'r' or op2 == 's' or op2 == 't' \
 or op2 == 'v' or op2 == 'w' or op2 == 'x' or op2 == 'y' or op2 == 'z':
    print('Sim')
else:
    print('Não')
