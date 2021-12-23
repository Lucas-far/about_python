

# Integração do bdd MySQL com um projeto que vai usá-lo (parte 1 - Instalação de dependências)
def parte_5():
    """
    • OBS: Antes de fazer os procedimentos, é preciso que um projeto Django tenha sido minimamente configurado
    • pip install mysqlclient PyMySQL (talvez a segunda dependência não precise ser adicionada)
    • pip freeze > requirements.txt
    """


# Configuração do banco de dados em um projeto Django [ NAME = nome do bdd criado na parte 1 ]
def pp_settings():
    """
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'nome_do_bdd_criado_pelo_user',
            'USER': 'nome_do_user_que_criou_o_bdd',
            'PASSWORD': 'senha_do_user_que_criou_o_bdd',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    """
