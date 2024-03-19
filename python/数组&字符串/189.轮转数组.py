class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 确保k在有效范围内，针对k大于数组长度的情况
        k %= len(nums) 
        nums[:] = nums[len(nums) - k :] + nums[: len(nums) - k]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    Solution().rotate(nums, k)
    print(nums)

    nums2 = [-1, -100, 3, 99]
    k2 = 2
    Solution().rotate(nums2, k2)
    print(nums2)

    nums3 = [1, 2]
    k3 = 5
    Solution().rotate(nums3, k3)
    print(nums3)
