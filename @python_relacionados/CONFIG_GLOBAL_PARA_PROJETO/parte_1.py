

# Instalação do Git
def git_instalar_windows():
    """
    - Baixar o Git em seu website
    - git --version

    ------------------------------------------------ COMANDOS OPCIONAIS ------------------------------------------------
    git config --global user.name 'nome_user_github   (Registrar ao git ao nome de usuário da sua conta Github)
    git config --global user.email 'email_user_github (Registrar o git ao email usado para criar a sua conta do Github)

    - Junto ao [ Git ] teremos o [ Git bash ] que é recomendável para a criação de uma chave SSH pelo Windows
    """


def git_instalar_ubuntu():
    """
    - sudo apt-get install git-all
    - git --version

    ------------------------------------------------ COMANDOS OPCIONAIS ------------------------------------------------
    git config --global user.name 'nome_user_github   (Registrar ao git ao nome de usuário da sua conta Github)
    git config --global user.email 'email_user_github (Registrar o git ao email usado para criar a sua conta do Github)
    """


# Criar uma conta Github (não necessita explicação) e criar uma chave SSH pessoal na sua conta Github
def criar_chave_ubuntu():
    """
    1 - Ir ao terminal, e executar o comando [ ssh-keygen -t rsa ]
        OBS: após "rsa", pode usar [ 'seu_email_github' ], mas não é mandatório

    2 - Digitar uma passphrase
        EXEMPLO: umafrasepodevalermuitacoisamasaomesmotempopodenaovalernada
        OBS: Após essa etapa, um diretório é criado em: [ /home/seu_user/.ssh ]

    3 - Serão criados: [ public key ] [ key fingerprint = SHA256 ] [ key's randomart ]

    4 - Ir ao diretório [ /home/seu_user/.ssh ], procurar por [ cat id_rsa.pub ], abrir e [ ctrl + c ]

    5 - Ir ao site do Github

    6 - Fazer o caminho: [ Avatar / Settings / SSH and GPG keys / New ssh key ]

    7 - No campo [ title ], dar o nome desejado à chave

    8 - No campo [ key ], [ ctrl + v ]

    9 - Salvar
    """


def criar_chave_windows():
    """
    - No Windows, ao instalar o [ Git ], também é instalado o [ Git bash ], então ele deve ser aberto
    - No [ Git bash ] executar [ ssh-keygen.exe -t rsa ]

    --------------------------- Etapas que acontecem após iniciar a criação de uma chave SSH ---------------------------
    Etapa 1: Enter file in which to save the key        [ pode ser ignorada = ENTER ]
    Etapa 2: Enter passphrase (empty for no passphrase) [ pode ser ignorada = ENTER ]
    Etapa 3: Enter same passphrase again:               [ pode ser ignorada = ENTER ]
    Etapa 4: Your identification has been saved in
    Etapa 5: Your public key has been saved in
    Etapa 6: The key fingerprint is:

    - Na etapa 5, o Git Bash mostra o caminho a ser copiado, que leva ao arquivo [ id_rsa.pub ]
    - Este arquivo deve ser aberto e seu conteúdo, copiado

    ------------------------------------------------ No site do Github ------------------------------------------------
    Avatar -> settings -> ssh and gpg keys -> new ssh key -> preencher nome -> preencher chave com o conteúdo copiado ->
    add ssh key

    - No campo [ title ], dar o nome desejado à chave
    - No campo [ key ], [ ctrl + v ]
    - Salvar
    """