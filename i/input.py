

# Input tipo 1    [referência única] [referência interna: %s] [referência externa: %]
nome = input('Qual o seu nome? -> ')
print('Obrigado, %s' % nome)

# Input tipo 1    [referência múltipla] [referência interna: %s] [referência externa: %]
nome = input('Qual o seu nome? -> ')
sobrenome = input('Qual o seu sobrenome? -> ')
print('Obrigado, %s %s' % (nome, sobrenome))

# Input tipo 2    [referência única] [referência interna: {}] [referência externa: .format(arg)]
nome = input('Qual o seu nome? -> ')
print('Obrigado, {}'.format(nome))

# Input tipo 2    [referência múltipla] [referência interna: {} {}] [referência externa: .format(arg, arg)]
nome = input('Qual o seu nome? -> ')
sobrenome = input('Qual o seu sobrenome? -> ')
print('Obrigado, {} {}'.format(nome, sobrenome))

# Input tipo 3    [referência única] [referência interna: f'{arg}']
nome = input('Qual o seu nome? -> ')
print(f'Obrigado, {nome}')

# Input tipo 3    [referência múltipla] [referência interna: f'{arg} {arg}']
nome = input('Qual o seu nome? -> ')
sobrenome = input('Qual o seu sobrenome? -> ')
print(f'Obrigado, {nome} {sobrenome}')
