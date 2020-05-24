def pair_sum(array, sum):
    array = sorted(array)
    left = 0
    right = len(array) - 1

    while left < right:
        if array[left] + array[right] == sum:
            return [array[left], array[right]]
        elif array[left] + array[right] < sum:
            left += 1
        else:
            right -= 1
    return [None, None]


def test_function(test_case):
    input_list = test_case[0]
    target = test_case[1]
    solution = test_case[2]
    output = pair_sum(input_list, target)
    if output == solution:
        print("Pass")
    else:
        print("False")


input_list = [2, 7, 11, 15]
target = 9
solution = [2, 7]
test_case = [input_list, target, solution]
test_function(test_case)


input_list = [0, 8, 5, 7, 9]
target = 9
solution = [0, 9]
test_case = [input_list, target, solution]
test_function(test_case)


input_list = [110, 9, 89]
target = 9
solution = [None, None]
test_case = [input_list, target, solution]
test_function(test_case)