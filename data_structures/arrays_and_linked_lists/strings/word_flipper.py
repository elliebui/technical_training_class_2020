

def word_flipper(our_string):

    """
    Flip the individual words in a sentence

    Args:
       our_string(string): Strings to have individual words flip
    Returns:
       string: String with words flipped

    return pass
    """
    sentence = our_string.split()

    # Reverse each word in sentence
    flipped_words = [word[::-1] for word in sentence]

    flipped_string = " ".join(flipped_words)

    return flipped_string


print("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")