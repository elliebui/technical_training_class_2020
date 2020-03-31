

def anagram_checker(str1, str2):

    """
    Check if the input strings are anagrams

    Args:
       str1(strings),str2(strings): Strings to be checked if they are anagrams
    Returns:
       bool: If strings are anagrams or not
    """

    # Remove all spaces in both strings and make all characters lowercase
    # Sort each character from 2 strings and compare
    sorted_str1 = sorted(str1.replace(" ", "").lower())
    sorted_str2 = sorted(str2.replace(" ", "").lower())

    return sorted_str1 == sorted_str2


print ("Pass" if not (anagram_checker('water','waiter')) else "Fail")
print ("Pass" if anagram_checker('Dormitory','Dirty room') else "Fail")
print ("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print ("Pass" if not (anagram_checker('A gentleman','Elegant men')) else "Fail")
print ("Pass" if anagram_checker('Time and tide wait for no man','Notified madman into water') else "Fail")
