#邻接矩阵
class solution:
    def find(self,x):
        n= x//2
        dp = [1, 1, 2]
        if n < 3:
            return dp[n]
        for i in range(3,n+1):
            cur = 0
            for j in range(0,i):
                cur = cur + dp[j]*dp[i-1-j]
            dp.append(cur)
        return dp[-1]
n = int(input())
print(solution().find(n))