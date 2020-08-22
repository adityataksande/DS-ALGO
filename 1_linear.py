# A simple approach to do linear search
# start with leftmost & compare each one by one.


def search(arr, n, x):
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1


arr = [2, 6, 7, 5, 8, 9, 4, 1]
x = 1
n = len(arr)
result = search(arr, n, x)
if(result == -1):
    print("Element is not present in the array")
else:
    print("Element is present in the array", result)
