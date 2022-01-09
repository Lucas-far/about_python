

def data_filter(input_text, target_data, text_for_error):
    """
    Ao invés de lidar com try e except, é melhor:
        Usar um input de str
        Inserir o valor desejado num iterável
        E, caso queira um valor inteiro, ele é convertido após a satisfação
    """

    target_box = (target_data, )

    age = input(input_text)

    if age in target_box:
        return int(age)
    else:
        print(text_for_error)
        return data_filter(input_text='Insira algo', target_data='18', text_for_error='Ocorreu um erro')


if __name__ == '__main__':
    var = data_filter(input_text='Insira algo\n-> ', target_data='18', text_for_error='Ocorreu um erro\n-> ')
