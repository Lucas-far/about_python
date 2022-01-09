

def mtd_check_accuracy_word_and_translation(group_words, group_words_translation):
    """
    Compares two lists, in which one must hold the words and another holds the translations
    It is recommended the two lists have the same length and the translations must be placed correctly
    The methods will test the accuracy between the indexes
    It is recommended the lists to not have repeated data
    """
    from random import choice
    word = choice(group_words)
    word_index = group_words.index(word)
    word_translation = group_words_translation[word_index]
    return f'{word}    {word_translation}'


if __name__ == '__main__':
    words = [1, 2, 3, 4, 5, 6, 7]
    translations = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
    print(var2 := mtd_check_accuracy_word_and_translation(group_words=words, group_words_translation=translations))
