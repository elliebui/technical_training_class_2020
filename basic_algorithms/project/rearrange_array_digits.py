from basic_algorithms.basic.heap_sort import heap_sort


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    len_list = len(input_list)
    first_num = 0
    second_num = 0
    sorted_list = heap_sort(input_list)

    for i in range(len_list - 1, -1, -1):
        if i % 2 == 0:
            first_num = first_num * 10 + sorted_list[i]
        else:
            second_num = second_num * 10 + sorted_list[i]

    return [first_num, second_num]

# Total time complexity: O(NlogN)
# heap_sort = O(NlogN)
    # heapify = O(logN), for loop = O(N)
# for loop = O(N)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
