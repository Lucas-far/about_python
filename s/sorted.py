

"""
Objetivo
    - Organizar dados em qualquer iterável
    - É preferencial que seja usada em lista e tupla

Observação
    - A ordenação leva em consideração letras maiúsculas como preferência
    - Funciona somente se todos os dados de um iterável forem do mesmo tipo

"""


def do_sort(container, inverter_ordem, ordem_por_tamanho):

    allowed_types = (
        "<class 'str'>", "<class 'tuple'>", "<class 'list'>", "<class 'set'>", "<class 'dict_items'>",
        "<class 'dict_keys'>", "<class 'dict_values'>", "<class 'dict'>"
    )

    container_type = str(type(container))

    if container_type in allowed_types:
        if not inverter_ordem and not ordem_por_tamanho:
            return sorted(container)                # Uso normal (crescente)
        elif not inverter_ordem and ordem_por_tamanho:
            return sorted(container, key=len)       # Uso com parâmetro [key=]
        elif inverter_ordem and not ordem_por_tamanho:
            return sorted(container, reverse=True)  # Uso reverse (decrescente)
    return 'O dado fornecido não é iterável'


if __name__ == '__main__':
    string_ = 'Evandro Saraiva Pedrosa de Figueiredo'
    tupla_ = ('Evandro,', 'Saraiva', 'Pedrosa', 'de', 'Figueiredo')
    lista_ = [data.lower() for data in tupla_]
    conjunto_ = {*tupla_}
    dicionario_com_itens = {2: 'dois', 3: 'três', 1: 'um'}.items()
    dicionario_com_chaves = {2: 'dois', 3: 'três', 1: 'um'}.keys()
    dicionario_com_valores = {2: 'dois', 3: 'três', 1: 'um'}.values()
    dicionario = {2: 'dois', 3: 'três', 1: 'um'}
    tupla2_ = ('a', 'aa', 'aaa', 'aaaa', 'aaaaa')

    # Teste da condição 1 e de todos os tipos compatíveis
    print('(1)    ', do_sort(container=string_, inverter_ordem=False, ordem_por_tamanho=False))
    print('(2)    ', do_sort(container=tupla_, inverter_ordem=False, ordem_por_tamanho=False))
    print('(3)    ', do_sort(container=lista_, inverter_ordem=False, ordem_por_tamanho=False))
    print('(4)    ', do_sort(container=conjunto_, inverter_ordem=False, ordem_por_tamanho=False))
    print('(5)    ', do_sort(container=dicionario_com_itens, inverter_ordem=False, ordem_por_tamanho=False))
    print('(6)    ', do_sort(container=dicionario_com_chaves, inverter_ordem=False, ordem_por_tamanho=False))
    print('(7)    ', do_sort(container=dicionario_com_valores, inverter_ordem=False, ordem_por_tamanho=False))
    print('(8)    ', do_sort(container=dicionario, inverter_ordem=False, ordem_por_tamanho=False))

    # Teste da condição 2
    print('(9)    ', do_sort(container=tupla2_, inverter_ordem=False, ordem_por_tamanho=True))

    # Teste da condição 3
    print('(10)    ', do_sort(container=tupla2_, inverter_ordem=True, ordem_por_tamanho=False))

    # Teste de tipo incompatível
    print('(11)    ', do_sort(container=True, inverter_ordem=False, ordem_por_tamanho=False))
