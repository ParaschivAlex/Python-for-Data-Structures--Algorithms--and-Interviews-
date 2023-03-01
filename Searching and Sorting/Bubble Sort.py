def bubble(arr):
    for i in range(0, len(arr) - 1):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


arr = [3, 2, 13, 4, 6, 5, 7, 8, 1, 20]
bubble(arr)
print(arr)
