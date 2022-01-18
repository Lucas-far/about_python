

# Função normal (parâmetros podem ou não ter argumentos nomeados)
def add_to_dictionary(where, key, value):
    where[key] = value


if __name__ == '__main__':
    var = {}
    print(var)
    add_to_dictionary(where=var, key=0, value=0)  # com
    print(var)
    add_to_dictionary(var, 1, 1)                  # sem
    print(var)
