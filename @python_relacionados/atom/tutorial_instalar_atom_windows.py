

def comandos_atom():
    """
    ctrl + shift + p                     || Abrir janela de pesquisa
    ctrl + ,                             || Abrir o "Settings"
    ctrl + , + "install"                 || Instalar pacotes (platformio-ide-terminal + script + atom-python-virtualenv)
    ctrl + , + "packages"                || Instalar pacotes (language-python)
    alt + shift + t                      || Abrir o terminal instalado
    ctrl + shift + b                     || Executar um script de python
    ctrl (segurar) + botão <-            || Selecionar range de um texto
    """


def configuracao_talvez_necessaria():
    """
    O Atom precisa ter ser executável adicionado a variável de ambiente para funcionar
    Muito provavelmente, ele fica na pasta 'AppData', que fica escondida
    Sendo assim, é provável que este tutorial seja necessário

    ----------------------------------------------------- TUTORIAL -----------------------------------------------------
    Ir ao seu user no SO [ex: C:\Users\seu_user]
    Exibir (aba)
        Opções (canto superior direito)
            Alterar opções de pasta e arquivos

    Opções de pasta
        Modo de exibição (aba)
            Configurações avançadas
                Mostrar arquivos, pastas e unidades ocultas

    Aplicar -> OK
    """


def acessar_executavel_atom():
    """
    No passo anterior, a pasta "AppData" se tornou disponível
    Vamos adentrar e copiar o caminho do executável do Atom
    O caminho, no meu caso, a ser copiado é: [ C:\Users\seu_user\AppData\Local\atom ]
    """


def adicionar_atom_var():
    """
    Meu computador (botão direito)
        propriedades
            configurações avançadas do sistema
                propriedades do sistema
                    variáveis de ambiente
                        variáveis do sistema
                            path (selecionar)
                                editar
                                    colar o caminho do passo anterior
    """


def windows8_path():
    """
    No windows 8, variáveis são criadas juntas, separadas por ";"
    Os 3 últimos caminhos são mandatórios para um funcionamento completo do Atom junto ao Python

    C:\Arquivos de Programas\Java\jdk-11.0.7\bin;
    C:\MinGW\bin;
    C:\Users\seu_user\AppData\Local\atom;                             [ Registrar Atom software ]
    C:\Users\seu_user\AppData\Local\Programs\Python\Python39\;        [ Registrar Python interpretador ]
    C:\Users\seu_user\AppData\Local\Programs\Python\Python39\Scripts; [ Registrar Python pip ]
    """


def virtualenv_configurar():
    """
    ctrl + , + "install" || Instalar pacote (atom-python-virtualenv)
    Após instalar o pacote, clicar em [ Settings ]
    The $HOME variable points to the user home folder = pasta container onde é configurada uma variável de user
                                                        [ EX: C:\Users\seu_user\seu_user_venv ]

    ----------------------------------------------------- PROJETO -----------------------------------------------------
    No Atom, criar uma pasta e selecioná-la
    Abrir o terminal e fazer [ mkvirtualenv nome_do_ambiente ]
    Packages (aba) -> virtualenv -> select -> ambiente (clicar)
    O ambiente carregará, e agora dependências podem ser instaladas de forma isolada
    """