

def mtd_get_input_integer_specific(input_text: str, initial_integer: int, last_integer: int):
    """
    To treat improper data (strings, floating, integers out of a certain range) while a proper integer number is not
    being provided.
    """

    integer_out_of_range = f"""
        \033[1:31m========== ERROR ==========\033[m
        The provided input is not in the suitable range: {initial_integer} to {last_integer}"""

    integer_unused = f"""
        \033[1:31m========== ERROR ==========\033[m
        The provided input must be an integer number: {initial_integer} to {last_integer}"""

    while True:
        try:
            the_input = int(input(input_text))
            if the_input in range(initial_integer, last_integer + 1):
                return the_input
            else:
                print(integer_out_of_range)
        except ValueError:
            print(integer_unused)


if __name__ == '__main__':

    text = f"""
    ----------------------------------- Em qual mês você nasceu? (digite de 1 a 12) -----------------------------------
    Clique após a seta e digite -> """

    var = mtd_get_input_integer_specific(input_text=text, initial_integer=1, last_integer=12)
    print(var)
