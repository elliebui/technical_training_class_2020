def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source)-1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center+1:], left+center+1)
    else:
        return recursive_binary_search(target, source[:center], left)


def find_first_occurence_index(target, source):
    """
    To find the _first occurrence of an element in a sorted array
    :param target:
    :param source:
    :return:    None if target is not found
                index of first occurrence of target
    """
    index = recursive_binary_search(target, source, 0)
    if not index:
        return None
    while source[index] == target:
        if index == 0:
            return 0
        if source[index-1] == target:
            index -= 1
        else:
            return index


list_with_multiple_occurrence = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
print(find_first_occurence_index(7, list_with_multiple_occurrence))  # Should return 3
print(find_first_occurence_index(9, list_with_multiple_occurrence))  # Should return None


def contains(target, source):
    def _contains(target, source):
        if len(source) == 0:
            return False
        center = (len(source) - 1) // 2
        if source[center] == target:
            return True
        elif source[center] < target:
            return _contains(target, source[center + 1:])
        else:
            return _contains(target, source[:center])
    return _contains(target, source)


letters = ['a', 'c', 'd', 'f', 'g']

print(contains('a', letters))  # True
print(contains('b', letters))  # False