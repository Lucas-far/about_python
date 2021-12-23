

def fonte():
    """
    Curso  # Programação em Python do básico ao avançado
    Seção  # Seção 24:Novidades do Python 3.8
    Aula   # 169. Tipos de dados mais precisos
    Tempo  # 03:45
    """

def infos():
    """
    Objetivo:
        verificar módulos com presença de tipagem, e retornar se a tipagem correta foi aplicada

    Objetivo 2:
        verificar módulos, para achar erros mais incomuns, não apresentados por uma IDE

    Instalação:
        pip install mypy

    Observação:
        1. Tipagem, não torna argumento mandatório para classe sugerida, então não gera-se erro, caso haja
        2. O recurso [ mypy ] torna-se necessário pelo fato da tipagem ser apenas instrutiva
        3. Para verificar módulos dentro de diretórios/diretórios aninhados, é preciso entrar neles pelo terminal
            Exemplo:
                pwd                         # /home/lucas/PycharmProjects/recursos
                cd PYTHON/p                 # muda-se para o diretório alvo
                pwd                         # /home/lucas/PycharmProjects/recursos/PYTHON/p
                ls                          # listam-se os módulos, para procurar o nome de um módulo alvo
                mypy 'pip install mypy.py'  # o nome do módulo PRECISA ser especificado em formato de string
    """

def mandar_mensagem(texto: str) -> str:
    return texto

print(mandar_mensagem(['Eu não gosto de panetone']))  # Há um erro aqui, mas não é anunciado na execução normal

# Qual seria a segunda opção de checagem? mypy
""" mypy 'pip install mypy.py' """

# Retorno
"pip install mypy.py:12: error:"
"Argument 1 to 'mandar_mensagem' has incompatible type 'List[str]'; expected 'str'"
"Found 1 error in 1 file (checked 1 source file)"
