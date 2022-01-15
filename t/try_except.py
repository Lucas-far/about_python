

"""
Objetivo:
   - Tratar blocos de código, para informar um erro: do sistema, customizado

Observação:
   - Sintaxes como essa: [ except (NameError, TypeError, ValueError): ] é possível
"""

try:
    null = 0
    print(null[0])
except TypeError as error_:
    two_erros = (
        f'------- Erro do sistema -------\n{error_}',
        "------- Erro customizado -------\nObjeto do tipo inteiro não é iterável para usar índexação"
    )
    for data in two_erros:
        print(data)
