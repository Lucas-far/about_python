

# Função normal (parâmetros após o asterisco devem ter argumentos nomeados)
def add_to_dictionary(where, *, key, value):
    where[key] = value


if __name__ == '__main__':
    try:
        var = {}
        print(var)
        add_to_dictionary(var, key=0, value=0)
        print(var)
        add_to_dictionary(var, 1, 1)
        print(var)

    except TypeError:
        print("TypeError: add_to_dictionary() got some positional-only arguments passed as keyword arguments: 'where'")
