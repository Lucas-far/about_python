

def objetivo():
    """ Exemplificar formas de uso da sintaxe desse recurso """

if __name__ == '__main__':

    # ------------------------- Exemplo de filtragem de dados com partes de uma palavra-chave -------------------------
    keyword = 'java'
    languages = ['Python', 'Java', 'JavaScript', 'C#', 'C++', 'Ruby']

    # Order      3    1                     2
    filtering = [dado for dado in languages if keyword in dado or keyword.title() in dado]

    print([1], filtering)

    # -------------------- Exemplo simples de list comprehension e loop for fazendo a mesma tarefa --------------------
    vogais = 'a e i o u'.split()
    vogais_cacha_alta = [dado.upper() for dado in vogais]
    print([2], vogais_cacha_alta)
    vogais_copia = 'a e i o u'.split()

    for index, data in enumerate(vogais_copia):
        vogais_copia[index] = data.upper()

    print([3], vogais_copia)
