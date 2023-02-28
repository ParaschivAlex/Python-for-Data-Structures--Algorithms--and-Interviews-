# Iterativ
def binary_search1(arr, ele):
    found = 0
    left = 0
    right = len(arr) - 1
    while not found and left <= right:
        mij = (left + right) // 2
        if arr[mij] == ele:
            found = 1
        elif ele < arr[mij]:
            right -= 1
        else:
            left += 1
    if found:
        return True
    else:
        return False


# Recursiv
def binary_search2(arr, ele):
    if len(arr) == 0:
        return False
    else:
        mij = len(arr) // 2
        if arr[mij] == ele:
            return True
        elif ele < arr[mij]:
            return binary_search2(arr[:mij], ele)
        else:
            return binary_search2(arr[mij+1:], ele)


# list must already be sorted!
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search1(arr, 4))
print(binary_search1(arr, 2.2))

print(binary_search2(arr, 4))
print(binary_search2(arr, 2.2))
