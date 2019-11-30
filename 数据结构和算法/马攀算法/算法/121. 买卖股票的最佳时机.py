class Solution:
    def maxProfit(self, prices) :
        dp = [[0, 0] for i in range(len(prices))]
        if not prices:
            return 0

        dp[0] = [0, -prices[0]]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        return dp[-1][0]

print(Solution().maxProfit([7,1,5,3,6,4]))

class Solution:
    def maxProfit(self, prices) :
        dp = [[0, 0] for i in range(len(prices))]
        if not prices:
            return 0
        dp[0] = [0, -prices[0]]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0]-prices[i])
        return dp[-1][0]