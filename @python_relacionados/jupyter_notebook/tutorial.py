

def fonte():
    """
    https://www.youtube.com/watch?v=H_pu_63qrS8
    How to Install Jupyter Notebook in Windows 10 | Install Jupyter Notebook Python 3.9
    """


# Talvez menos eficiente
def forma_1():
    """
    1. Instalar o python (lembrar de marcar [ Add python to PATH ]) no instalador
    2. Ir a pasta de scripts do python [ C:\Users\seu_user\AppData\Local\Programs\Python\Python39\Scripts ]
    3. Copiar esse caminho
    4. Abrir o terminal e fazer [ cd caminho copiado ]
    5. Estando na pasta de Scripts do python pelo terminal, fazer [ pip install jupyter ]
    5. A instalação é demorada
    6. Criar uma pasta no diretório de usuário, entrar nessa pasta, clicar na barra de endereço, digitar [ cmd ]
    6. Ao fazer isso, é aberto o [ terminal ] dentro daquele caminho onde o comando [ cmd ] foi feito
    7. Digitar no terminal o comando [ jupyter notebook ]
    7. Se tudo der certo, haverá um retorno com um link onde há o nome [ localhost ]. Ele deve ser copiado
    8. Colar o link [ localhost ] em um navegador
    9. Além disso, é preciso ter registrado o token, que também é disponível no terminal, após a criação do notebook
    9. No terminal, procurar por [ token= ] e copie o código que vêm após essa sintaxe, caso precise relogar
    """


# Talvez mais eficiente
def forma_2():
    """
    - Criar uma pasta e entrar nela pelo terminal
    - python -m venv nome_do_ambiente      (Serve para Windows e Ubuntu)
    - nome_do_ambiente\scripts\activate    (Windows)
    - source nome_do_ambiente/bin/activate (Ubuntu)
    - Estando com o ambiente ativado, fazer [ python -m pip install --upgrade pip ]

    ----------------------------------------------------- DETALHE -----------------------------------------------------
    É preciso associar o ambiente virtual criado localmente no SO com um [ Jupyter notebook ]
    Todos os comandos abaixo devem ser feitos com o ambiente virtual ativado

    - pip install ipykernel
    - python -m ipykernel install --user --name=nome_do_ambiente
    - jupyter notebook
    - Copiar o link disponível no terminal referente a [ localhost ], e abrir em um navegador
    - Você será redirecionado a um Jupyter notebook, funcionando como uma IDE
    - Se você deslogar pelo botão [ logout ] na tela, o link torna-se [ http://localhost:8888/logout ]
    - Para relogar deve-se clicar em [ login page ], porém você precisa ter um acesso via [ token ]
    - Abra o terminal e digite [ jupyter notebook list ]
    - Será mostrado todos os [ jupyter notebooks ] existentes no SO
    - Copie a parte do link que vêm após a sintaxe [ token= ] e cole no campo [ Password or Token ] na página de login
    - Você voltara ao ambiente que você criou

    ----------------------------------------------------- DETALHE -----------------------------------------------------
    - Qualquer arquivo [ python ] criado, ao ser acessado, precisa estar configurado p/ execução pelo ambiente virtual
    - Para isso, abra este arquivo no Jupyter. Na aba [ Kernel ] fazer [ change kernel ] [ clicar no ambiente virtual ]
    - O comando ativa o ambiente virtual no [ computador jupyter ] e configura ele p/ executar arquivos python
    """
