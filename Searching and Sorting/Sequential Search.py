# Unordered List
def seq_search1(arr, ele):
    for elem in arr:
        if elem == ele:
            return True
    return False


# Ordered List
def seq_search2(arr, ele):
    i = 0
    while arr[i] <= ele and i < len(arr) - 1:
        if arr[i] == ele:
            return True
        i += 1
    else:
        return False


arr = [1, 9, 2, 8, 3, 4, 7, 5, 6]
print(seq_search1(arr, 1))
print(seq_search1(arr, 10))

print(seq_search2(arr, 1))
print(seq_search2(arr, 10))
