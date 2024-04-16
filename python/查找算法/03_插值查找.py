def insert_value_search(arr, left, right, num):
    if left > right or left >= len(arr) or right < 0:
        return -1

    mid = left + (num - arr[left]) * (right - left) // (arr[right] - arr[left])
    if mid >= len(arr) or mid < 0:
        return -1

    if arr[mid] == num:
        return mid
    elif arr[mid] > num:
        return insert_value_search(arr, left, mid - 1, num)
    else:
        return insert_value_search(arr, mid + 1, right, num)

arr = [1, 2, 3, 4, 5]
num = 3
print(insert_value_search(arr, 0, len(arr) - 1, num))  # 2