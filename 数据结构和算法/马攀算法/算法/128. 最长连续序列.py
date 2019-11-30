'''
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。


'''
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        用哈希表存储每个端点值对应连续区间的长度
若数已在哈希表中：跳过不做处理
若是新数加入：
取出其左右相邻数已有的连续区间长度 left 和 right
计算当前数的区间长度为：cur_length = left + right + 1
根据 cur_length 更新最大长度 max_length 的值
更新区间两端点的长度值
'''

        max_num = 0
        dic ={}
        for i in nums:
            if i not in dic:
                left = dic.get(i-1,0)  #若i-1存在返回value  否则返回0
                right = dic.get(i+1,0)
                cur_length = left + right +1
                if cur_length  > max_num:
                    max_num = cur_length
                dic[i] = cur_length
                dic[i-left] = cur_length
                dic[i+right] = cur_length
        print(dic)
        return max_num
a = Solution().longestConsecutive([1,2,8,1,3,5,4,7])
print(a)
