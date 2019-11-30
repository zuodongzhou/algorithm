
'''
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
思想：维护一个i结尾的最大书，和最小数，不停的更新。
'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = nums[0]
        min_num = nums[0]
        count = nums[0]
        for i in nums[1:]:
            max_end = max_num
            min_end =  min_num
            max_num = max(i,i*max_end,i*min_end)
            min_num = min(i,i*max_end,i*min_end)
            if max(max_num, min_num) > count:
                count = max(  max_num, min_num    )
        return count