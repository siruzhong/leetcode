def counting_sort(arr, exp):
    """
    对数组中的每个元素按照指定的位数进行排序

    :param arr: 输入的数组
    :param exp: 指定的位数
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # 计算每个元素在指定位数下的数值，并统计每个数值出现的次数
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # 计算每个数值的起始索引
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 将元素按照指定位数的数值放入输出数组中
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # 将排序后的数组复制回原数组
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    """
    基数排序

    :param arr: 输入的数组
    """
    max_val = max(arr)
    exp = 1

    # 从最低位开始，依次进行排序
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# 示例
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("原始数组:", arr)
radix_sort(arr)
print("基数排序后的数组:", arr)