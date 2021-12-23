

def infos():
    """
    Objetivo:
        converter uma classe para outra
    """

# tupla para conjunto
def declarar():
    print('|| 1 ||', exemplo := set((1, 2, 7)))  # || 1 || {1, 2, 7}

# conjunto para lista
def print_():
    print('|| 2 ||', list({*range(1, 11)}))  # || 2 || [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# string para inteiro
def redeclarar():
    print('|| 3 ||', exemplo := '151120', '#####', exemplo := int(exemplo))  # || 3 || 151120 ##### 151120

# lista para string
def var_nova():
    print('|| 4 ||', exemplo := ['abc'], '#####', exemplo2 := ' '.join(exemplo))  # || 4 || ['abc'] ##### abc

declarar(), print_(), redeclarar(), var_nova()
