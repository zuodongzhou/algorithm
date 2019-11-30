
#给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
class Solution:
    def firstMissingPositive(self, nums):
        length = len(nums)
        if length == 0:
            return 1
        i = 0
        while i < length:
            if nums[i] == i+1 :
                i += 1
            else:
                if 0 < nums[i] <length:
                    if nums[nums[i]-1] == nums[i]:
                        i += 1
                    else:
                        nums[nums[i] - 1],nums[i] = nums[i],nums[nums[i] - 1]
                else:
                    i+=1
        for i , num in enumerate(nums):
            if num != i+1:
                return i+1
        return length +1
print(Solution().firstMissingPositive([3,4,-1,1]))