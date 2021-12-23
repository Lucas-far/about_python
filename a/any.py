

"""
Objetivo:
    converter todos os dados dentro de variáveis iteráveis ou literais para booleano...
    se há pelo menos um dado = True, então o método retorna = True...
    Se todos os dados = False, então o método retorna = False

Observação:
    1. se o método receber um parâmetro que não é uma classe iterável, ele gera [ TypeError ]
    """

# @dict @list @set @str @tuple

print(f"{any({'': ''}) = }")  # any({'': ''}) = False
print(f"{any([]) = }")        # any([]) = False
print(f"{any({}) = }")        # any({}) = False
print(f"{any('') = }")        # any('') = False
print(f"{any(()) = }")        # any(()) = False

# Quando há, entre os índices, algum verdadeiro = True
exemplo = [(), [], '', ' ']
for x in exemplo:
    print(x, '=', any(x))
print('Resultado:', any(exemplo))

# Quando nenhum dos índices é verdadeiro = False
exemplo2 = [(), [], '']
for x in exemplo2:
    print(x, '=', any(x))
print('Resultado 2:', any(exemplo2))
