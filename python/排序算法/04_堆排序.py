def heapify(arr, n, i):
    # arr: 待调整的数组
    # n: 数组的长度
    # i: 当前需要调整的节点索引

    # 找到左子节点和右子节点的索引
    left = 2 * i + 1
    right = 2 * i + 2

    # 初始化最大值的索引为当前节点
    largest = i

    # 如果左子节点存在且大于当前最大值，更新最大值索引
    if left < n and arr[i] < arr[left]:
        largest = left

    # 如果右子节点存在且大于当前最大值，更新最大值索引
    if right < n and arr[largest] < arr[right]:
        largest = right

    # 如果最大值索引发生变化，交换当前节点和最大值节点的值，并递归调整以最大值节点为根的子树
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    # arr: 待排序的数组

    # 计算数组长度
    n = len(arr)

    # 从最后一个非叶子节点开始，自底向上地调整堆结构
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 进行堆排序的主要步骤
    for i in range(n - 1, 0, -1):
        # 将堆顶元素（最大值）与末尾元素交换
        arr[i], arr[0] = arr[0], arr[i]
        # 将剩余n-1个元素重新调整为堆
        heapify(arr, i, 0)

# 测试数组
arr = [12, 11, 13, 5, 6, 7]
# 调用堆排序函数
heap_sort(arr)
# 输出排序后的数组
print("Sorted array is:", arr)