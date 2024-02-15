def find_duplicate1(nums):
    res = []
    num_set = set()
    for num in nums:
        if num in num_set:
            res.append(num)
        num_set.add(num)
    return res


def find_duplicate2(nums):
    res = []
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            res.append(nums[i])
    return res


nums = [1, 3, 4, 2, 2, 3]
print(type(nums))
print(find_duplicate1(nums))  # [2, 3]
print(find_duplicate2(nums))  # [2, 3]
