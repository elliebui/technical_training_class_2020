def smallest_positive(in_list):
    # This function defines a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.

    result = None

    for number in in_list:
        if number > 0:
            if result is None:
                result = number
            elif number < result:
                result = number
 
    return result

# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

print(smallest_positive([-6, -9, -7]))
# Correct output: None

print(smallest_positive([]))
# Correct output: None
