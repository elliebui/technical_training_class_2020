def square_root(n):
    low = 1
    high = n
    ans = 0

    if n == 0 or n == 1:
        return n

    while low <= high:
        mid = (low + high) // 2
        if mid * mid == n:
            return mid
        if mid * mid < n:
            low = mid + 1
            ans = mid
        else:
            high = mid - 1

    return ans


print("Pass" if (3 == square_root(9)) else "Fail")
print("Pass" if (0 == square_root(0)) else "Fail")
print("Pass" if (4 == square_root(16)) else "Fail")
print("Pass" if (1 == square_root(1)) else "Fail")
print("Pass" if (5 == square_root(27)) else "Fail")

# Time complexity: This algorithm is using low-mid-high to eliminate
# half of the search elements, its run time is O(logN)
