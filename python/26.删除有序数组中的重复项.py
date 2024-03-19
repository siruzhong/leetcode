class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pt = 0
        # 避免数组只有一个元素的情况
        while pt < len(nums) and len(nums) > 1:
            if nums[pt] == nums[pt - 1]:
                nums.pop(pt)
            else:
                pt += 1


if __name__ == "__main__":
    nums = [1, 1, 2]
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    Solution().removeDuplicates(nums)
    print(nums)
    Solution().removeDuplicates(nums2)
    print(nums2)
