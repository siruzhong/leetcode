def fibonacci_search(arr, num):
    # 初始化斐波那契数列的前两个元素
    fib_m_minus_2 = 0
    fib_m_minus_1 = 1
    fib_m = fib_m_minus_1 + fib_m_minus_2

    # 计算斐波那契数列，直到找到一个大于等于数组长度的斐波那契数
    while fib_m < len(arr):
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib_m
        fib_m = fib_m_minus_1 + fib_m_minus_2

    # 初始化索引
    index = -1

    # 当斐波那契数列的长度大于1时，继续查找
    while fib_m > 1:
        # 计算子序列的索引
        i = min(index + fib_m_minus_2, len(arr) - 1)

        # 如果目标值小于子序列的中间元素，调整搜索范围
        if arr[i] < num:
            fib_m = fib_m_minus_1
            fib_m_minus_1 = fib_m_minus_2
            fib_m_minus_2 = fib_m - fib_m_minus_1
            index = i
        # 如果目标值大于子序列的中间元素，调整搜索范围
        elif arr[i] > num:
            fib_m = fib_m_minus_2
            fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
            fib_m_minus_2 = fib_m - fib_m_minus_1
        # 如果找到目标值，返回其索引
        else:
            return i

    # 如果在最后一个子序列中找到目标值，返回其索引
    if fib_m_minus_1 and index < len(arr) - 1 and arr[index + 1] == num:
        return index + 1

    # 如果没有找到目标值，返回 -1
    return -1

arr = [1, 2, 3, 4, 5]
num = 3
print(fibonacci_search(arr, num))  # 2