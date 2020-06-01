def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    low_index = 0
    mid_index = 0
    high_index = len(input_list) - 1
    while mid_index <= high_index:
        if input_list[mid_index] == 0:
            input_list[mid_index], input_list[low_index] = input_list[low_index], input_list[mid_index]
            low_index += 1
            mid_index += 1
        elif input_list[mid_index] == 2:
            input_list[high_index], input_list[mid_index] = input_list[mid_index], input_list[high_index]
            high_index -= 1
        else:
            mid_index += 1
    return input_list

# Time complexity: O(N) since we're traversing through input list once


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
