
'''
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

'''


class Solution:
    def generateMatrix(self, n):
        dp = [[0] * n for i in range(n)]
        x1, y1, x2, y2 = 0, 0, n - 1, n - 1
        num = 1

        while x2 >= x1 and y2 >= y1:
            num = self.test(num, x1, y1, x2, y2, dp)
            x1 += 1
            y1 += 1
            x2 -= 1
            y2 -= 1
        if n % 2 == 1:
            dp[x1 - 1][y1 - 1] = num
        return dp

    def test(self, n, x1, y1, x2, y2, dp):
        for i in range(y1, y2):
            dp[x1][i] = n
            n += 1
        for i in range(x1, x2):
            dp[i][y2] = n
            n += 1
        for i in range(y2, y1, -1):
            dp[x2][i] = n
            n += 1
        for i in range(x2, x1, -1):
            dp[i][y1] = n
            n += 1
        return n