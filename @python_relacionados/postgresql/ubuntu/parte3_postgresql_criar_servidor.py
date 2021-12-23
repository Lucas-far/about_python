

# Configuração de um servidor para um usuário 'não root' existente
def parte_1():
    """
    ----------------------------------------------------- DETALHES -----------------------------------------------------
    • As informações abaixo só fazem sentido se já existe um usuário 'não root' criado
    • A ideia é a de que o servidor seja configurado com as mesmas credenciais do usuário 'não root'

    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    • Servers -> botão direito -> create -> server

    --------------------------------------------------- CONFIGURAÇÃO ---------------------------------------------------
    • General    || Name              || nome do usuário 'não root' + server
    • Connection || Host name/address || localhost
    • Connection || Username          || nome do usuário 'não root'
    • Connection || Password          || senha do usuário 'não root'
    • [ Save ]
    """
