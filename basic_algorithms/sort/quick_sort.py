def partition(array, l, h):
    pivot = array[(l+h)//2]
    i = l
    j = h
    while i < j:
        while i < h and array[i] < pivot:
            i += 1
        while j > l and array[j] >= pivot:
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]

    array[l], array[j] = array[j], array[l]
    return j


def quick_sort(array, l, h):
    if l < h:
        j = partition(array, l, h)
        quick_sort(array, l, j)
        quick_sort(array, j+1, h)


items = [8, 3, 1, 7, 0, 10, 2]
quick_sort(items, 0, len(items) - 1)
print(items)

items = [1, 0]
quick_sort(items, 0, len(items) - 1)
print(items)

items = [96, 98, 97]
quick_sort(items, 0, len(items) - 1)
print(items)

items = []
quick_sort(items, 0, len(items) - 1)
print(items)

items = [1]
quick_sort(items, 0, len(items) - 1)
print(items)