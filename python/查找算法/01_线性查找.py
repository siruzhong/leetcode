def seq_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1

arr = [1, 2, 3, 4, 5]
num = 3
print(seq_search(arr, num)) # 2