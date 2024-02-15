def reverse1(arr):
    for i in range(len(arr) // 2):  # // rounds down to the nearest whole number
        arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]
    return arr

def reverse2(arr):
    return arr[::-1]

arr1 = [1, 2, 3, 4, 5]
print(reverse1(arr1)) # [5, 4, 3, 2, 1]

arr2 = [1, 2, 3, 4, 5]
print(reverse2(arr2)) # [5, 4, 3, 2, 1]