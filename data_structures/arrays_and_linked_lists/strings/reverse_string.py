

def string_reverser(our_string):
    """
    Reverse the input strings

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed strings
    """

    return our_string[::-1]

# Test Cases


print("Pass" if ('retaw' == string_reverser('water')) else "Fail")
print("Pass" if ('!noitalupinam sgnirts gnicitcarP' == string_reverser('Practicing strings manipulation!')) else "Fail")
print("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")


"""
Answer:
Pass
Pass
Pass
"""