class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pt1, pt2 = 0, 0
        while pt1 < len(nums):
            times = 0
            while pt1 < len(nums) and nums[pt1] == nums[pt2]:
                if times + 1 < 3:
                    times += 1
                    pt1 += 1
                else:
                    nums.pop(pt1)
            pt2 += times


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    Solution().removeDuplicates(nums)
    print(nums)
    nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    Solution().removeDuplicates(nums2)
    print(nums2)
