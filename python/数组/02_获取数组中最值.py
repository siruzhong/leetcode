def get_max_value(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

def get_min_value(arr):
    min = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min


arr = [1, 2, 3, 4, 5]
print(get_max_value(arr))
print(get_min_value(arr))