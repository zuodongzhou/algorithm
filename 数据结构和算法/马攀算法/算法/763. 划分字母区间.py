'''
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。

示例 1:

输入: S = "ababcbacadefegdehijhklij"
输出: [9,7,8]
解释:
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。


'''
'''
用字典存储每个字符最后的位置
从第一个字符开始遍历，每获取一个字符就寻找该字符最后一次出现的位置索引，
并将其定为当前片段的最后位置，在达到该位置之前， 继续寻找更靠后的最后位置，
若达到最后位置之前都没有发现更靠后的最后位置，则将当前最后位置作为一个片段的末尾， 
前个片段的末尾后一位是该片段的开头。 实际上是贪心算法思想的一次运用，
在每一步中得到截止目前为止的局部最优解，后一个最优解总是比前一个最优解“更优”， 
由此推进到结束时，便可得到全局最优解。



'''
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dic = {}
        for i ,s1 in enumerate(S):
                dic[s1] = i
        result = []
        cur = dic[S[0]]
        for i ,s1 in enumerate(S):
            if dic[s1] > cur :
                cur = dic[s1]
            if i == cur :
                result.append(cur+1-sum(result))
        return result