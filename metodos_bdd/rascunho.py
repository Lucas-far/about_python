

def mtd_get_string_specific(input_text: str, allowed_words: list, single_word: bool):
    """
    To treat improper data (strings, floating, integers out of a certain range) while a proper integer number is not
    being provided.
    """

    paragraphy = '    '

    str_invalid = f"""
    O texto digitado é inválido. A(s) palavra(s) permitida(s) é/são:\n"""

    # integer_unused = f"""
    # \033[1:31m========== ERROR ==========\033[m
    # O que foi digitado não é um dado de texto"""

    while True:
        if single_word:
            # print('Verdade')
            the_input = str(input(input_text))
            for word in allowed_words:
                if word == the_input:
                    return the_input

                else:
                    print(str_invalid)
                    print(paragraphy, allowed_words)
                    # for word in allowed_words:
                    #     print(paragraphy + word)

        else:
            # print('Falso')
            the_input = str(input(input_text))
            for word in allowed_words:
                if word == the_input:
                    return the_input
            else:
                print(str_invalid)
                print(paragraphy, allowed_words)
                # for word in allowed_words:
                #     print(paragraphy + word)


if __name__ == '__main__':

    text = f"""
    ----------------------------------- Você está vivo? -----------------------------------
    Clique após a seta e digite -> """

    # var = mtd_get_string_specific(input_text=text, allowed_words=['sim'], single_word=True)
    var2 = mtd_get_string_specific(input_text=text, allowed_words=['sim', 'não'], single_word=False)
    # print(var)
    print(var2)
