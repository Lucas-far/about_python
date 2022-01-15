

"""
Objetivo
    - Organizar dados em qualquer iterável
    - É preferencial que seja usada em lista e tupla
    - Se o parâmetro usado for usado em um conjunto, é preciso fazer um casting para funcionar (ver # EXEMPLO)

Observação
    - A ordenação leva em consideração letras maiúsculas como preferência
    - Funciona somente se todos os dados de um iterável forem do mesmo tipo
"""


def seek_for_ending(container, ending, class_):

    box_result = sorted(container, key=lambda var: ending in var, reverse=True)

    if class_ == 'lista':
        box_result = list(box_result)
        return box_result
    elif class_ == 'tupla':
        box_result = tuple(box_result)
        return box_result
    elif class_ == 'conjunto/lista':    # EXEMPLO
        box_result = list(box_result)
        return box_result
    elif class_ == 'conjunto/tupla':    # EXEMPLO
        box_result = tuple(box_result)
        return box_result


if __name__ == '__main__':
    conjunto = {"Oftalmologista", "Professor", "Dentista", "Arquiteto", "Legista", "Advogado", "Frentista", "Prefeito"}
    lista = "Oftalmologista Professor Dentista Arquiteto Legista Advogado Frentista Prefeito".split()
    tupla = ("Oftalmologista", "Professor", "Dentista", "Arquiteto", "Legista", "Advogado", "Frentista", "Prefeito")

    print(seek_for_ending(container=conjunto, ending='ista', class_='conjunto/lista'))  # EXEMPLO
    print(seek_for_ending(container=conjunto, ending='ista', class_='conjunto/tupla'))  # EXEMPLO
    print(seek_for_ending(container=lista, ending='ista', class_='lista'))
    print(seek_for_ending(container=tupla, ending='ista', class_='tupla'))
