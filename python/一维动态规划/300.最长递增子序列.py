class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * (len(nums))
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    # dp[i] 表示以 nums[i] 结尾的最长上升子序列的长度
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(Solution().lengthOfLIS(nums))
    nums2 = [0, 1, 0, 3, 2, 3]
    print(Solution().lengthOfLIS(nums2))
    nums3 = [7, 7, 7, 7, 7, 7, 7]
    print(Solution().lengthOfLIS(nums3))
