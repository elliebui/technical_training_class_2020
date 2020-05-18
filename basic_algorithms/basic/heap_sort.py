def heap_sort(arr):
    n = len(arr)

    # create a max-heap
    # don't need to loop through the 2nd half of array since those leaf nodes are heaps already
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # create sorted array in ascending order
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def heapify(arr, n, i):
    """
    :param: arr - array to heapify
    n -- number of elements in the array
    i -- index of the current node
    Converts an array (in place) into a maxheap, a complete binary tree with the largest values at the top
    """
    # consider current index as largest element
    largest_index = i
    left_node_index = 2 * i + 1
    right_node_index = 2 * i + 2

    # if current node has left child and its value is less than its left child
    # assign left node index as largest element
    if left_node_index < n and arr[i] < arr[left_node_index]:
        largest_index = left_node_index

    # if current node has right child and its largest element (itself or its left child) is less than its right child
    # assign right node index as largest element
    if right_node_index < n and arr[largest_index] < arr[right_node_index]:
        largest_index = right_node_index

    # if either of left or right child is the largest node
    # swap current node with that child, and heapify again, with updated largest_index
    if largest_index != i:
        arr[i], arr[largest_index] = arr[largest_index], arr[i]
        heapify(arr, n, largest_index)


def test_function(test_case):
    heap_sort(test_case[0])
    if test_case[0] == test_case[1]:
        print("Pass")
    else:
        print("False")


arr = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
solution = [0, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]
test_case = [arr, solution]
test_function(test_case)

arr = [5, 5, 5, 3, 3, 3, 4, 4, 4, 4]
solution = [3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
test_case = [arr, solution]
test_function(test_case)

arr = [99]
solution = [99]
test_case = [arr, solution]
test_function(test_case)

arr = [0, 1, 2, 5, 12, 21, 0]
solution = [0, 0, 1, 2, 5, 12, 21]
test_case = [arr, solution]
test_function(test_case)
