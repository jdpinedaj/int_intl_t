import string


def replace_words(sentence) -> str:
    """
    Replace each word in a sentence with a new word that has the first letter, the last letter, and the number of distinct characters in between.

    :param sentence: The sentence to replace words in
    :return: The sentence with the words replaced

    >>> replace_words("Smooth")
    'S3h'
    >>> replace_words("Space separated")
    'S3e s5d'
    >>> replace_words("Dash-separated")
    'D2h-s5d'
    >>> replace_words("Number2separated")
    'N4r2s5d'
    """
    # Create a string of separators that includes punctuation, whitespace, and digits
    separators = string.punctuation + string.whitespace + string.digits

    # Initialize the result string and the starting position of the current word
    result = ''
    word_start = 0

    # Loop through each character in the sentence
    for i in range(len(sentence)):
        if sentence[i] in separators:
            word_end = i
            if word_end > word_start:
                word = sentence[word_start:word_end]
                first_letter = word[0]
                last_letter = word[-1]
                distinct_chars = set(word[1:-1])
                count = str(len(distinct_chars))
                new_word = first_letter + count + last_letter
                result += new_word + sentence[word_end]
            # If the word has only one character (i.e. it's just a separator), add it to the result string
            else:
                result += sentence[word_end]
            word_start = word_end + 1

    # Handle the last word in the sentence (if it exists)
    if word_start < len(sentence):
        word = sentence[word_start:]
        first_letter = word[0]
        last_letter = word[-1]
        distinct_chars = set(word[1:-1])
        count = str(len(distinct_chars))
        new_word = first_letter + count + last_letter
        result += new_word

    # Return the result string
    return result


# Asserting
assert replace_words("Smooth") == "S3h"
assert replace_words("Space separated") == "S3e s5d"
assert replace_words("Dash-separated") == "D2h-s5d"
assert replace_words("Number2separated") == "N4r2s5d"
