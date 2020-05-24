def sort_012(input_list):
    low = 0
    mid = 0
    high = len(input_list) - 1
    while mid <= high:
        if input_list[mid] == 0:
            input_list[mid], input_list[low] = input_list[low], input_list[mid]
            low += 1
            mid += 1
        elif input_list[mid] == 2:
            input_list[high], input_list[mid] = input_list[mid], input_list[high]
            high -= 1
        else:
            mid += 1
    return input_list


def test_function(test_case):
    sort_012(test_case)
    print(test_case)
    if test_case == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_case = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
test_function(test_case)

test_case = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
test_function(test_case)

test_case = [2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1]
test_function(test_case)
