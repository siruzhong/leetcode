class Solution(object):
    # 递归
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    # 动态规划
    def climbStairs2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        # 创建一个长度为 n+1 的列表，并将所有元素初始化为 0
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

if __name__ == "__main__":
    print(Solution().climbStairs(3))
    print(Solution().climbStairs(4))
    print(Solution().climbStairs(5))