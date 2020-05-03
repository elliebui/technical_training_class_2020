def staircase(n):
    num_dict = dict()
    return _staircase(n, num_dict)


def _staircase(n, num_dict):
    if n == 1:
        result = 1
    elif n == 2:
        result = 2
    elif n == 3:
        result = 4
    else:
        if (n - 1) in num_dict:
            result_1 = num_dict[n - 1]
        else:
            result_1 = _staircase(n - 1, num_dict)

        if (n - 2) in num_dict:
            result_2 = num_dict[n - 2]
        else:
            result_2 = _staircase(n - 2, num_dict)

        if (n - 3) in num_dict:
            result_3 = num_dict[n-3]
        else:
            result_3 = _staircase(n - 3, num_dict)

        result = result_1 + result_2 + result_3

    num_dict[n] = result

    print(num_dict)
    return result


def test_function(test_case):
    answer = staircase(test_case[0])
    if answer == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_case = [3, 4]
test_function(test_case)

test_case = [4, 7]
test_function(test_case)

test_case = [5, 13]
test_function(test_case)

test_case = [20, 121415]
test_function(test_case)


