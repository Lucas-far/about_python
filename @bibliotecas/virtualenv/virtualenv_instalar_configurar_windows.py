

def python_instalar():
    """
    1 - Baixar o python (não esquecer de marcar [ add python to PATH ] na instalação)
    2 - O python precisa de duas variáveis de sistema: uma para o interpretador, e a outra para o pip

    Interpretador || C:\Users\nome_user\AppData\Local\Programs\Python\Python39
    Pip           || C:\Users\Conta secundária\AppData\Local\Programs\Python\Python39\Scripts

    ------------------------------------------------------- OBS -------------------------------------------------------
    - O path do interpretador já deve vir configurado, mas caso não seja, fazer através do caminho especificado acima

    3- Ao final da instalação, abrir o terminal e testar comandos
       [ python / python -V / pip -V / pip install --upgrade pip ]
    """


def terminal():
    """
    Com o pip do Python instalado, é possível instalar dependências, neste caso a que criar ambientes virtuais

    pip install virtualenv
    pip install virtualenvwrapper-win
    """


def windows():
    """
    ----------------------------------------------------- PARTE 1 -----------------------------------------------------
    Criar uma pasta para ser container de ambientes virtuais
    Não é mandatório, mas é útil que a pasta seja criada no diretório do seu usuário
    Não é mandatório, mas é útil que o nome da pasta seja [ Envs ]
    Um exemplo de caminho criado, seria [ C:\Users\seu_user\Envs ]

    ----------------------------------------------------- PARTE 2 -----------------------------------------------------
    Criação de uma variável de usuário

    Meu computador (botão direito)
        propriedades
            configurações avançadas do sistema
                propriedades do sistema
                    variáveis de ambiente
                        variáveis de usuário
                            novo

    Nome da variável  || Qualquer nome em cacha alta [ exemplo: WORKON_HOME ]
    Valor da variável || Caminho especificado na parte 1
    OK

    ----------------------------------------------------- PARTE 3 -----------------------------------------------------
    No terminal, [ echo %nome da variável criada na parte 2% ]
    O retorno desse comando deve ser o próprio nome da variável de usuário, para mostrar que ela está sendo recocnhecida

    ----------------------------------------------------- PARTE 4 -----------------------------------------------------
    Agora é preciso iniciar um projeto

    ----------------------------------------------------- Pycharm -----------------------------------------------------
    Há a vantagem de ter a opção [ New environment using: virtualenv ] (após instalar a dependência do virtualenv)
    Pode ser ignorado o uso do comando [ mkvirtualenv nome_do_ambiente ]
    Ao criar um projeto usando a opção mencionado, ao abrir, estará disponível o ambiente virtual [ venv ]
    Ambiente virtual (ativar)    [ venv\scripts\activate ]
    Ambiente virtual (desativar) [ deactivate ]

    ------------------------------------------------------- Atom -------------------------------------------------------
    MENOS RECOMENDÁVEL
    Se for optado por criar um ambiente virtual via terminal pelo comando [ mkvirtualenv nome_do_ambiente ] dentro do
    projeto, então será criada uma pasta em [ C:\Users\seu_user\Envs ] onde será inserido esse ambiente novo (a criação
    da pasta "Envs" só acontece caso seja a primeira vez criando um ambiente virtual pelo comando acima, caso contrário,
    apenas a pasta do ambiente virtual é criado dentro da pasta principal "Envs")

    MAIS RECOMENDÁVEL
    Se for optado por criar um ambiente virtual via menu [ Packages / Virtualenv / Make ] dentro do projeto, então a
    pasta desse ambiente virtual será criada no caminho especificado no pacote instalado [ atom-python-virtualenv ],
    nos seus [ Settings ]

    Ambiente virtual (ativar) [ Packages / Virtualenv / Select ]
    """
