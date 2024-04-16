def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            key = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > key:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = key
        gap //= 2
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print("原始数组：", arr)
print("希尔排序后的数组：", shell_sort(arr)) # [11, 12, 22, 25, 34, 64, 90]