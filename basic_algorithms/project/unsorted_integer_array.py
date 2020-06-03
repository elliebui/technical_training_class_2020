## Example Test Case of Ten Integers
import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    n = len(ints)

    if n == 0:
        return
    elif n == 1:
        return ints[0], ints[1]

    if ints[0] < ints[1]:
        min_int = ints[0]
        max_int = ints[1]
    else:
        max_int = ints[0]
        min_int = ints[1]

    for num in ints[2:]:
        if num < min_int:
            min_int = num

        if num > max_int:
            max_int = num

    return min_int, max_int
# Time complexity is O(N) since we're only traversing through the list once


l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
