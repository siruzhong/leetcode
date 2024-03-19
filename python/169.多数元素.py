class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        # 因为多数元素的个数大于n/2，所以排序后的中间元素一定是多数元素
        # //代表向下除法向下取整，math.ceil(x/y)代表向上取整
        return nums[len(nums) // 2]


if __name__ == "__main__":
    nums = [3, 2, 3]
    print(Solution().majorityElement(nums))
    nums1 = [2, 2, 1, 1, 1, 2, 2]
    print(Solution().majorityElement(nums1))
