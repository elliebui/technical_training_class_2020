## Example Test Case of Ten Integers
import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    n = len(ints)

    if len(ints) == 0:
        return
    elif len(ints) == 1:
        return ints[0], ints[1]
    else:
        if ints[0] < ints[1]:
            min = ints[0]
            max = ints[1]
        else:
            max = ints[0]
            min = ints[1]

    for i in range(2, n):
        if ints[i] < min:
            min = ints[i]

        if ints[i] > max:
            max = ints[i]

    return min, max
# Time complexity is O(N) since we're only traversing through the list once


l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
