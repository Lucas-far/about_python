
"""
Objetivo:
    - Criar e gerenciar senhas

Observação:
    - Funcional em diferentes paradigmas de programação
"""


def create_password(view_it):
    from passlib.hash import pbkdf2_sha256 as tier

    input_text = 'Por favor, insira uma senha após a seta -> '
    this_warning = 'Senha criada.'
    this_input = input(input_text)
    password_ = tier.hash(this_input, rounds=200_000, salt_size=16)

    if view_it:
        return password_
    return this_warning


def verify_password(passphrase_guess, passphrase_current):

    from passlib.hash import pbkdf2_sha256 as tier

    this_msg_success = 'Verificação realizada. Acesso permitido.'
    this_msg_failure = 'Verificação realizada. Acesso negado.'

    is_it_correct = tier.verify(passphrase_guess, passphrase_current)
    if is_it_correct:
        return this_msg_success
    return this_msg_failure


class Login:

    from passlib.hash import pbkdf2_sha256 as tier

    this_msg_success = 'Verificação realizada. Acesso permitido.'
    this_msg_failure = 'Verificação realizada. Acesso negado.'

    def __init__(self, key):
        self.__key = Login.tier.hash(key, rounds=200_000, salt_size=16)

    def verify_password_v2(self, data_key):
        analysis = Login.tier.verify(data_key, self.__key)
        if analysis:
            return Login.this_msg_success
        return Login.this_msg_failure


if __name__ == '__main__':
    a_password = create_password(view_it=True)
    a_verification = verify_password(passphrase_guess='Python', passphrase_current=a_password)
    print(a_password)
    print(a_verification)  # O resultado depende no que será colocado no input

    print('_' * 100)

    pessoa = Login(key='dubistnichtmeinvatter')
    print(pessoa.verify_password_v2(data_key='password.'))
    print(pessoa.verify_password_v2(data_key='dubistnichtmeinvatter'))
