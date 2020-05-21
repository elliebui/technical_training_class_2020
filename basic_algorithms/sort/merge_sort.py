def merge_sort(items):
    # Base case, a list of 0 or 1 items is already sorted
    if len(items) <= 1:
        return items

    # Otherwise, find the midpoint and split the list
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    # Call mergesort recursively with the left and right half
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge our two halves and return
    return merge(left, right)


def merge(left, right):
    # Given two ordered lists, merge them together in order,
    # returning the merged list.
    out_list = list()
    left_index = 0
    right_index = 0

    # Move through the lists until we have go append all items from one list in out_list
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            out_list.append(left[left_index])
            left_index += 1
        else:
            out_list.append(right[right_index])
            right_index += 1

    # Append any leftovers. Because we've broken from our while loop,
    # we know at least one is empty, and the remaining:
    # a) are already sorted
    # b) are all larger than our last element in out_list
    out_list += left[left_index:]
    out_list += right[right_index:]

    return out_list


test_list_1 = [8, 3, 1, 7, 0, 10, 2]
test_list_2 = [1, 0]
test_list_3 = [97, 98, 99]
print('{} to {}'.format(test_list_1, merge_sort(test_list_1)))
print('{} to {}'.format(test_list_2, merge_sort(test_list_2)))
print('{} to {}'.format(test_list_3, merge_sort(test_list_3)))
