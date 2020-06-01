def bubble_sort_1(l):
    n = len(l)
    # go through each element
    for i in range(n - 1):
        # since last i elements are already in place, we don't need to go through them again
        for j in range(n - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]


wakeup_times = [16, 49, 3, 12, 56, 49, 55, 22, 13, 46, 19, 55, 46, 13, 25, 56, 9, 48, 45]


bubble_sort_1(wakeup_times)
print("Pass" if (wakeup_times[0] == 3) else "Fail")

# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24, 13), (21, 55), (23, 20), (22, 5), (24, 23), (21, 58), (24, 3)]


def bubble_sort_2(l):
    n = len(l)
    # go through each element
    for i in range(n - 1):
        # since last i elements are already in place, we don't need to go through them again
        for j in range(n - i - 1):
            if l[j][0] < l[j + 1][0]:
                l[j], l[j + 1] = l[j + 1], l[j]
            elif l[j][0] == l[j + 1][0] and l[j][1] < l[j + 1][1]:
                l[j], l[j + 1] = l[j + 1], l[j]


bubble_sort_2(sleep_times)
print("Pass" if (sleep_times == [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)]) else "Fail")