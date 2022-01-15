

"""
Objetivo:
    - Converter um dado string para lista

Observação:
    - Pode ou não, receber um separador como parâmetro
    - O dado recebido como parâmetro (o separador), é excluído no momento da conversão
"""


def converter_para_lista(separar, separador, texto_):

    try:
        if separar:
            return texto_.split(separador)  # Uso aqui
        return texto_.split()               # Uso aqui
    except AttributeError:
        return 'Tipo de dado permitido: somente string'


if __name__ == '__main__':
    texto = 'Python é uma linguagem de programação'
    print(converter_para_lista(separar=True, separador='a', texto_=texto))
    print(converter_para_lista(separar=False, separador=None, texto_=texto))
    print(converter_para_lista(separar=False, separador=None, texto_=tuple(texto)))
    print(converter_para_lista(separar=False, separador=None, texto_=set(texto)))
