

from random import choice

# ------------------------ Usando dicionário com uma chave matriz para chamar chaves aleatórias ------------------------
pronouns = {
    'pronouns': {
        'I (início da frase)': 'Eu', 'You (singular)': 'Você', 'He': 'Ele', 'She': 'Ela', 'It': 'Isso', 'We': 'Nós',
        'You (plural)': 'Vocês', 'They': 'Eles(as)', 'I': 'eu', 'you (singular)': 'você', 'he': 'ele', 'she': 'ela',
        'it': 'isso', 'we': 'nós', 'you (plural)': 'vocês', 'they': 'eles(as)'
    }
}

pronoun_key = choice(list(pronouns['pronouns'].keys()))  # precisa haver um construtor para acessar as chaves aninhadas
pronoun_value = pronouns['pronouns'][pronoun_key]        # então, a chave gerada acima é passada aqui
print(pronoun_key, pronoun_value)                        # na impressão, vemos que os dados condizem
