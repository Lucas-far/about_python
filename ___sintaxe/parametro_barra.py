

# Função normal (parâmetros após a barra podem ter argumentos nomeados)
def add_to_dictionary(where, /, key, value):
    where[key] = value


if __name__ == '__main__':
    try:
        var = {}
        print(var)
        add_to_dictionary(var, 0, 0)
        print(var)
        add_to_dictionary(where=var, key=1, value=1)
        print(var)

    except TypeError:
        print("TypeError: add_to_dictionary() got some positional-only arguments passed as keyword arguments: 'where'")
