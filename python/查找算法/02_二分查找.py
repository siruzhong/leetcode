def binary_search(arr, left, right, num):
    mid = (left + right) // 2
    if left > right:
        return -1
    if arr[mid] == num:
        return mid
    elif arr[mid] > num:
        return binary_search(arr, left, mid - 1, num)
    else:
        return binary_search(arr, mid + 1, right, num)
    
arr = [1, 2, 3, 4, 5]
num = 3
print(binary_search(arr, 0, len(arr) - 1, num)) # 2