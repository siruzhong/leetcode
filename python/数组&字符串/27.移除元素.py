class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pt = 0
        while pt < len(nums):
            if nums[pt] == val:
                nums.pop(pt)
            else:
                pt += 1

    # 优化：不使用pop()方法，而是使用双指针
    def removeElement2(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pt1, pt2 = 0, 0
        while pt1 < len(nums):
            if nums[pt1] != val:
                nums[pt2] = nums[pt1]
                pt2 += 1
            pt1 += 1
        nums[:] = nums[:pt2]


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    Solution().removeElement2(nums, val)
    Solution().removeElement2(nums2, val2)
    print(nums)
    print(nums2)
