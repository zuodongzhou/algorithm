'''
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

'''
#思想 动态规划：
'''
定义一个与输入数组+1的dp数组，
dp[i] 代表小偷从第1号到第i号屋子偷钱的最大收益。
可简单推理出，如果偷了第i号屋子，
收益为nums[i-1] + dp[i-2] (因为相邻不可偷)。
如果不偷，收益为dp[i-1]. 逐步求最大值即可。

'''
class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        result = [0,nums[0],max(nums[0],nums[1])]
        for i in range(3,len(nums)+1):
            result.append(max(result[i-2]+nums[i-1],result[i-1]))
        return result[-1]