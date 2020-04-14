
def reverse_string(input):
    """
    Return reversed input string

    Examples:
       reverse_string("abc") returns "cba"

    Args:
      input(str): string to be reversed

    Returns:
      a string that is the reverse of input
    """

    n = len(input)

    if n <= 1:
        return input
    else:
        return input[-1] + reverse_string(input[:(n-1)])



# Test Cases

print("Pass" if ("" == reverse_string("")) else "Fail")
print("Pass" if ("cba" == reverse_string("abc")) else "Fail")
print("Pass" if ("dcba" == reverse_string("abcd")) else "Fail")

# Another way
# def reverse_string(input):
#
# if len(input) <= 0:
#     return input
# else:
#     return reverse_string(input[1:]) + input[0]
