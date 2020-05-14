def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return -1
    center = (len(source)-1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center+1:], left+center+1)
    else:
        return recursive_binary_search(target, source[:center], left)


def find_first_occurrence_index(target, source):
    """
    To find the _first occurrence of an element in a sorted array
    :param target:
    :param source:
    :return:    None if target is not found
                index of first occurrence of target
    """
    index = recursive_binary_search(target, source, 0)
    if index == -1:
        return -1
    while source[index] == target:
        if index == 0:
            return 0
        if source[index-1] == target:
            index -= 1
        else:
            return index


def find_last_occurrence_index(target, source):
    """
    To find the _last occurrence of an element in a sorted array
    :param target:
    :param source:
    :return:    None if target is not found
                index of last occurrence of target
    """
    index = recursive_binary_search(target, source, 0)

    if index == -1:
        return -1
    while source[index] == target:
        if index == len(source) - 1:
            return len(source) - 1
        if source[index+1] == target:
            index += 1
        else:
            return index


def find_first_and_last_occurrence_index(target, source):
    first_index = find_first_occurrence_index(target, source)
    last_index = find_last_occurrence_index(target, source)
    print(first_index, last_index)
    return [first_index, last_index]


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = find_first_and_last_occurrence_index(number, input_list)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


input_list = [1]
number = 1
solution = [0, 0]
test_case_1 = [input_list, number, solution]
test_function(test_case_1)


input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number = 3
solution = [3, 6]
test_case_2 = [input_list, number, solution]
test_function(test_case_2)

input_list = [0, 1, 2, 3, 4, 5]
number = 5
solution = [5, 5]
test_case_3 = [input_list, number, solution]
test_function(test_case_3)

input_list = [0, 1, 2, 3, 4, 5]
number = 6
solution = [-1, -1]
test_case_4 = [input_list, number, solution]
test_function(test_case_4)
