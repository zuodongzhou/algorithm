class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
        for i, k in enumerate(dp[0]):
            dp[0][i] = i
        for j, k in enumerate(range(len(word1) + 1)):
            dp[j][0] = j
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                dp[i][j] = min(dp[i - 1][j]+1  , dp[i][j - 1]+1 ,dp[i - 1][j - 1] + (1 if word1[i-1] != word2[j-1] else 0))
        print(dp)
        return dp[-1][-1]
'''
当 min(i, j) \ne 0 的时候，lev_{a,b}(|a|, |b|) 为如下三项的最小值：
1.lev_{a,b}(i-1, j) 表示 删除 a_i,将str[:i-1]再变化为 STR2[j]  ,加 1
2.lev_{a,b}(i, j-1) 表示 先把str[:i],编辑为str2[:j-1] 再  插入 b_j
3.dp[i - 1][j - 1] + (1 if word1[i-1] != word2[j-1] else 0) 表示  如果相等  则等于前面dp[i-1][j-1],如果不相等，则等于先编辑dp[i-1][j-1] 再把str[i]替换 b_j
'''
word1 ,word2 = "horse","sor"
a = Solution().minDistance(word1 ,word2 )
print(a)