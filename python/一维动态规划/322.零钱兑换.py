class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 创建一个长度为 amount+1 的列表，并将所有元素初始化为正无穷
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        # 遍历硬币列表
        for coin in coins:
            # 遍历金额
            for i in range(coin, amount + 1):
                # dp[i]值：表示不使用当前硬币coin的情况下组成金额i所需的最少硬币数量
                # dp[i-coin]+1：表示使用当前硬币coin的情况下组成金额i所需的最少硬币数量
                # 选择较小的值作为新的dp[i]值
                dp[i] = min(dp[i], dp[i - coin] + 1)
        # 如果dp[amount]值没有发生改变，说明没有任何一种硬币组合能组成金额amount
        return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print(Solution().coinChange(coins, amount))
    coins2 = [2]
    amount2 = 3
    print(Solution().coinChange(coins2, amount2))
    coins3 = [1]
    amount3 = 0
    print(Solution().coinChange(coins3, amount3))
