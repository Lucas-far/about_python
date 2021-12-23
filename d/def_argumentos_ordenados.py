

"""
Objetivo
    ordenar os tipos de parâmetros da forma correta, para não haver erros na execução da função
"""

# Qual a ordem dos parâmetros? [ obrigatoriedade de argumento ] [ classe aceita ] [ detalhe ]
"par 1: [ obrigatório     ] [ qualquer classe   ] [ é obrigatorio, por não ter um valor definido                  ]"
"par 2: [ não obrigatório ] [ qualquer classe   ] [ se não há parâmetros, o parâmetro recebe uma tupla vazia      ]"
"par 3: [ não obrigatório ] [ qualquer classe   ] [ não é obrigatorio, por ter um valor definido                  ]"
"par 4: [ não obrigatório ] [ classe dicionário ] [ se não há parâmetros, o parâmetro recebe uma dicionário vazio ]"

# Função com todos os tipos de parâmetro
def ordem(par, *args, par2=None, **kwargs):
    return par, args, par2, kwargs

# Argumentos após *args/tupla devem ser nomeados, para serem identificados, caso contrário, será uma tupla eterna
print(var := ordem('a', 'b', 'c', 'd', par2='e', f='g'))

# Parâmetro obrigatório
def obrig(par):
    return par
print(1, obrig([]))

# Parâmetro *args
def p_args(*args):
    return args
print(2, p_args(False, None, True))

# Parâmetro não obrigatório
def n_obrig(nome='não informado'):
    return nome
print(3, n_obrig())

# Parâmetro **kwargs
def p_kwargs(**kwargs):
    return kwargs
print(4, dicio := p_kwargs(nome='Lucas', idade=28, nacionalidade='Brasileiro'))

# Se a função tiver um objeto instanciado, é possível acessar dados singularmente
print(5, dicio['nome'])
print(6, dicio['idade'])
print(7, dicio['nacionalidade'])
