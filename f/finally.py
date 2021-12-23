

"""
Objetivo:
    lançar uma mensagem alternativa após o tratamento de um erro específico

Observação:
    1. [ finally ] existe quando [ try ] e [ except ] são usados, mas [ finally ] não baseia-se neles
"""

# Exemplo com erro
try:
    nome = 'Lucas'
    print(nome[-7])
except IndexError as index:
    print(f'===== Erro padrão IDE: =====\n{index}')  # Erro da IDE em uma variável
    print('===== Erro customizado =====\nO dado iterável escolhido não possui essa quantidade de índices')
finally:
    print('===== Mensagem alternativa usando o recurso [finally] =====\nErro tratado com sucesso!')

# Exemplo sem erro (apenas o print em finally é visto)
try:
    nome = 'Lucas'
    print(nome[0])
except IndexError as index:
    print(f'===== Erro gerado pela IDE: =====\n{index}')
    print(f'===== Erro =====\nO dado iterável escolhido não possui essa quantidade de índices')
finally:
    print(f'===== Mensagem alternativa usando o recurso [finally] =====\nErro tratado com sucesso!')
