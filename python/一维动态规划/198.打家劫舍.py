class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        dp = [0] * (length + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, length + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

        return dp[length]

    def rob2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        return max(
            self.rob(nums[: length - 1]),
            nums[length - 1] + self.rob(nums[: length - 2]),
        )


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    nums2 = [2, 7, 9, 3, 1]
    print(Solution().rob(nums))
    print(Solution().rob(nums2))
