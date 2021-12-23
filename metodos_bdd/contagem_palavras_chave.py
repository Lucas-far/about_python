

def texto_contar_palavra(the_text: str, keyword: str, not_allowed_special_characters: tuple, plural: str = 's'):
    """
    :param the_text: text where a keyword will be searched
    :param keyword: keyword to be searched
    :param plural: the plural form of the keyword, if there is one
    :param not_allowed_special_characters: list of characters to be excluded in the text, in order to cancel their
                                           countage, because they aren't actual words
    :return: var presenting the countage of occurences of the keyword
    """

    # The text must be neuter (lower cased), because python makes difference between lower and uppercased strings
    the_text = the_text.lower()

    # Replace specific special characters, because they will count as words if they are not removed (more can be added)
    for character in not_allowed_special_characters:
        the_text = the_text.replace(character, '')

    # Place all words into a list, so a countage can be performed
    text_converted_to_list = the_text.split()

    # From the list, the keyword will be counted and displayed (the sum from singular and plural forms together)
    countage_singular = text_converted_to_list.count(keyword)
    countage_plural = text_converted_to_list.count(keyword + plural)
    countage_both = countage_singular + countage_plural

    resultado = f"""
    Palavra procurada              || {keyword} / {keyword + plural}
    Núm. de ocorrências (singular) || {keyword} [{countage_singular}] vez(es)
    Núm. de ocorrências (plural)   || {keyword + plural} [{countage_plural}] vez(es)
    Núm. de ocorrências (ambas)    || {keyword}/{keyword + plural} [{countage_both}] vez(es)
    """

    return resultado


if __name__ == '__main__':

    text = """
    Operadores de String
    Python oferece operadores para processar texto (ou seja, valores de string). Assim como os números, as strings podem
    ser comparadas usando operadores de comparação: ==, !=, <, > e assim por diante. O operador ==, por exemplo, retorna
    True se as strings nos dois lados do operador tiverem o mesmo valor (Perkovic, p. 23, 2016).
    """

    print(texto_contar_palavra(the_text=text,
                               keyword='string',
                               not_allowed_special_characters=(',', '.', '(', ')', '\n'),
                               plural='s'))
