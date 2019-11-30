class Solution:
    def find(self,nums):
        dp = [ [0,0]  for i in range(len(nums))     ]
        dp[0][0] = nums[0][0]+ nums[0][2]
        dp[0][1] = nums[0][1]
        for i in range(1,len(nums)):
            dp[i][0] = min(dp[i-1][0]+nums[i][0],dp[i-1][1] + nums[i][0]+ nums[i][2])
            dp[i][1] = min(dp[i-1][1]+nums[i][1],dp[i-1][0] + nums[i][1]+ nums[i][2])
        return min(dp[-1])
a = [[20,40,20],[10,4,25],[90,10,5]]
print(Solution().find(a))
# 在你面前依次排着n棵树，而你有两种工具，锯子和斧头，它们砍第i棵树的时间分别为ai和bi，
# 一开始你拿的是斧头，而砍第i棵树前交换工具需要花费ci的时间，问题来了，依次砍完这些树的时间最短为多少呢？
# 3
# 20 40 20
# 10 4 25
# 90 100 5

# 第一行一个数n(n<=100)
# 接下来n行，每行3个数ai，bi，ci(<=30000)
# 一个数最短时间
