class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.pow(x, -n)
        else:
            return self.pow(x, n)

    def pow(self,x, n):
        if n == 1:
            return x
        elif n == 0:
            return 1
        else:
            if n % 2 == 1:
                return self.pow(x, n // 2) ** 2 * x
            else:
                return self.pow(x, n // 2) ** 2
print(Solution().myPow(2.0,10))