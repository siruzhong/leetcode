def search_in_two_dimensional_arrary(arr, target):
    i, j = len(arr) - 1, 0
    while i >= 0 and j < len(arr[0]):
        if arr[i][j] == target:
            return True
        if arr[i][j] > target:
            i -= 1
        if arr[i][j] < target:
            j += 1
    return False


arr = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16], [10, 13, 14, 17], [18, 21, 23, 26]]
print(search_in_two_dimensional_arrary(arr, 19))  # False
print(search_in_two_dimensional_arrary(arr, 13))  # True