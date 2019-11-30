class Solution:
    def maxProfit(self, prices) :
        dp = [[0, 0] for i in range(len(prices))]
        if not prices or len(prices)==1:
            return 0
        dp[0] = [0, -prices[0]]
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
        dp[1][1] = max(dp[0][1], dp[0][0]-prices[1])
        if len(prices)==2:
            return dp[1][0]
        for i in range(2, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0]-prices[i])
        return dp[-1][0]
print(Solution().maxProfit([1,2]))