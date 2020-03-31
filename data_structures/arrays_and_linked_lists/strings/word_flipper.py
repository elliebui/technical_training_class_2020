# Solution

def word_flipper(our_string):

    """
    Flip the individual words in a sentence

    Args:
       our_string(string): Strings to have individual words flip
    Returns:
       string: String with words flipped

    return pass
    """
    flipped_string = ""

    sentence = our_string.split(" ")

    for word in sentence:
        for i in range(1, len(word)):
            flipped_string += word[-i]

        flipped_string += word[0]
        flipped_string += " "

    # Remove the last space " "
    return flipped_string[:-1]


print("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")