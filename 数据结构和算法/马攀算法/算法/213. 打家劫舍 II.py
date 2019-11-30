class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def find(nums):
            dp = [0,nums[0],max(nums[0],nums[1])]
            for i in range(3,len(nums)+1):
                dp.append(max( dp[i-2] + nums[i-1],dp[i-1] ))
            return dp[-1]
        if len(nums) <= 0:return 0
        if len(nums) == 1:return nums[0]
        if len(nums) == 2:return max(nums[0],nums[1])
        return max(find(nums[1:]),find(nums[:-1]))