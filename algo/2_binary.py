# Given sorted array
data = [2, 4, 6, 8, 10, 11, 15, 17, 21, 25, 35, 41]
# Given Target
target = 35


def linear_search(data, target):
    for i in range:
        if data[i] == target:
            return True
    return False

# But we cannot consider linear search in worst case
# For binary search the array must be sorted


def binary_search_iterative(data, target):
    low = 0
    high = len(data)-1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return False


print(binary_search_iterative(data, target))

# Recursive Binary Search


def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid-1)
        else:
            return binary_search_recursive(data, target, mid+1, high)


print(binary_search_recursive(data, target, 0, len(data)-1))
