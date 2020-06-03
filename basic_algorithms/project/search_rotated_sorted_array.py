def search_rotate_sorted_array(arr, key):
    low_index = 0
    high_index = len(arr) - 1

    while low_index <= high_index:
        mid_index = (low_index + high_index) // 2

        if arr[mid_index] == key:
            return mid_index

        if arr[low_index] <= arr[mid_index]:  # if left subarr is sorted
            if arr[low_index] <= key < arr[mid_index]:
                high_index = mid_index
            else:
                low_index = mid_index + 1
        else:  # if right subarr is sorted
            if arr[mid_index] < key <= arr[high_index]:
                low_index = mid_index
            else:
                high_index = mid_index - 1

    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == search_rotate_sorted_array(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[6, 7, 8, 1, 2, 3, 4], 4])

# Time complexity: Since this algorithm is binary search, its time complexity is O(logN)
