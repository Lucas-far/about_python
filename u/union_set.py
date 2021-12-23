

def objetivo():
    """
    Unir dados não reincidentes de diferentes conjuntos
    """


if __name__ == '__main__':

    nome, sobrenome, complemento = {'Lucas'}, {'Farias'}, {'Santos de Sousa'}
    print([1], nome_completo := nome.union(sobrenome, complemento))

    eu = {'Lucas', 'Farias', 'Santos', 'de', 'Sousa'}
    mae = {'Maria', 'do', 'Rosário'}
    madrinha = {'Maria', 'Flôr'}

    print([2], fusao_nomes := eu.union(mae, madrinha))
