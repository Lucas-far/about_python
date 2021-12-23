

def fonte():
    """
    https://www.youtube.com/watch?v=yqkISICHH-U
    Tensorflow Object Detection in 5 Hours with Python | Full Course with 3 Projects
    """


def procedimentos():
    """
    1. Install and setup
    2. Collect Images and Label
    3. Training models
    4. Detecting objects
    5. Freezing and conversion
    6. Performance Tuning
    7. Training on Colab
    8. Projects

    ----------------------------------------------------- PROJETOS -----------------------------------------------------
    Tensorflow Object Detection Python Course Code: https://github.com/nicknochnack/TFODCourse
    Tensorflow Object Detection React App: https://github.com/nicknochnack/TFODApp
    Tensorflow Object Detection for Raspberry Pi: https://github.com/nicknochnack/TFODRPi
    """


def requisitos():
    """
    1. Visual C++ build tools
        https://visualstudio.microsoft.com/vs/community

    2. CUDA and cuDNN version
        https://www.tensorflow.org/install/source         (Ubuntu)
        https://www.tensorflow.org/install/source_windows (Windows)

    - Os softwares no item 2 oferecem aceleração em GPU para que o 'Tensorflow' treine seus modelos de detecção de objetos
    - Usar GPU é mais rápido do que usar a CPU e memória crua do computador
    - É preciso checar a versão do [ Tensorflow ] e mapear as bibliotecas apropriadas do CUDA e cuDNN
    - Nos links no item 2, na parte de baixo da página, é possível encontrar a configuração apropriada para cada versão do
      Tensorflow
    """


def parte_1():
    """
    - Criar uma pasta e entrar nela pelo terminal
    - git clone escolher_link_nos_procedimentos (No tutorial foi escolhido o link 1)
    - python -m venv projeto_jupyter_venv       (Última sintaxe é o nome do ambiente)              (Windows e Ubuntu)
    - projeto_jupyter_venv\scripts\activate     (Primeira sintaxe é o nome do ambiente)            (Windows)
    - source projeto_jupyter_venv/bin/activate  (Sintaxe 1 é fixa, Sintaxe 2 é o nome do ambiente) (Ubuntu)
    - Estando com o ambiente ativado, fazer [ python -m pip install --upgrade pip ]

    ----------------------------------------------------- DETALHE -----------------------------------------------------
    É preciso associar o ambiente virtual criado localmente no SO com um [ Jupyter notebook ]
    Todos os comandos abaixo devem ser feitos com o ambiente virtual ativado

    - pip install ipykernel
    - python -m ipykernel install --user --name=projeto_jupyter_venv (Última sintaxe é o nome do ambiente)
    - jupyter notebook (comando tanto para criar, quanto para entrar)
    - Copiar o link disponível no terminal referente a [ localhost ], e abrir em um navegador
    - Depois de entrar, voltar ao terminal e procurar pela informação [ 302 GET ] e copiar os caracteres após a palavra
      [ token= ]
    - EXEMPLO: [ token=2013ac3cd69993d615ea14b0cade02efb62fcbf357388e86 ]
    - Se você deslogar [ logout ], o link torna-se [ http://localhost:8888/logout ], então se deve clicar em
      [ login page ] para retornar ao ambiente Jupyter
    - Ao abrir a página de login, há o campo [ Password or Token ], então inserir os caracteres gerados pelo token
    """
