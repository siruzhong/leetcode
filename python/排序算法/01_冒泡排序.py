def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        flag = False    # 用于标记是否有数据交换
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if flag == False:   # 如果没有数据交换，说明数组已经有序
            break

arr = [64, 34, 25, 12, 22, 11, 90]
print("原始数组：", arr)
bubble_sort(arr)
print("冒泡排序后的数组：", arr)