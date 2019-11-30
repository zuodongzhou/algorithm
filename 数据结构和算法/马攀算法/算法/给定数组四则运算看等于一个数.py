
class Solution:

    def diffWaysToCompute(self, input,t):

        self.compute(input,t)

        return self.compute(input,t)

    def compute(self, input,t):
        if len(input) == 1 :
            if input[0] == t:#这里可以加一个判断
                return True
            else:
                return False
        for i in range(len(input) - 1):
            a = self.compute(input[:i] + [input[i] - input[i + 1]] + input[i + 2:],t)
            b = self.compute(input[:i] + [input[i] + input[i + 1]] + input[i + 2:],t)
            c = self.compute(input[:i] + [input[i] * input[i + 1]] + input[i + 2:],t)
        return a or b or c
print(Solution().diffWaysToCompute([1,1,1],3))