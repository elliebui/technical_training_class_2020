

def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    # Number of steps we have to take
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right)//2
        if array[middle] == target:  # found the target
            return middle
        elif array[middle] > target:  # if middle element is greater than target
            right = middle - 1  # look at the left half of array
        elif array[middle] < target:  # if middle element is less than target
            left = middle + 1  # look at the right half of array
    return -1


def test_function(test_case):
    answer = binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


target = 6
index = 6

array_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_case_1 = [array_1, target, index]
test_function(test_case_1)  # Pass

array_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
test_case_2 = [array_2, target, index]
test_function(test_case_2)  # Pass

array_3 = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
test_case_3 = [array_3, target, index]
test_function(test_case_3)  # Fail


def binary_search_recursive(array, target, left, right):
    '''Write a function that implements the binary search algorithm using recursion

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    if left > right:
        return -1

    middle = (left + right)//2

    if array[middle] == target:  # found the target
        return middle
    elif array[middle] > target:
        return binary_search_recursive(array, target, left, middle - 1)
    elif array[middle] < target:
        return binary_search_recursive(array, target, middle + 1, right)


def test_function(test_case):
    answer = binary_search_recursive(test_case[0], test_case[1], 0, (len(test_case[0]) - 1))
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


target = 4
index = 4

array_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
test_case_1 = [array_1, target, index]
test_function(test_case_1)  # Pass

array_2 = [0, 1, 2, 3, 5, 5, 6, 7, 8, 9]
test_case_2 = [array_2, target, index]
test_function(test_case_2)  # Fail


array_3 = [0, 1, 2, 3, 3.5, 5, 6, 7, 8, 9]
test_case_3 = [array_3, target, index]
test_function(test_case_3)  # Fail
