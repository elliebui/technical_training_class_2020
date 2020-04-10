"""
Write a function that takes a list and returns a new list that contains all the elements of the first list
minus all the duplicates. The order should remain the same.
"""


def get_list_without_duplicate(input_list):
    new_list = []
    for item in input_list:
        if item not in new_list:
            new_list.append(item)

    return new_list


# Test
list_a = [1, 3, 3, 5, 2, 5, 7, 8, 6]
list_b = ['a', 'z', 'd', 's', 'a', 'h', 's']

print(get_list_without_duplicate(list_a))
print(get_list_without_duplicate(list_b))

"""
Answer:
[1, 3, 5, 2, 7, 8, 6]
['a', 'z', 'd', 's', 'h']
"""