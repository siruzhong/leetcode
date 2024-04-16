def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# 示例
arr = [64, 34, 25, 12, 22, 11, 90]
print("原始数组：", arr)
selection_sort(arr)
print("选择排序后的数组：", arr) # [11, 12, 22, 25, 34, 64, 90]