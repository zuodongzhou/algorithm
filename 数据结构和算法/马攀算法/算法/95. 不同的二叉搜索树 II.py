# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def generateTrees(self, n) :
        if n == 0:
            return []
        input_ = [i+1 for i in range(n)]
        return self.find(input_)

    def find(self, input):
        if input == []:
            return [None]
        result = []
        for i in range(len(input)):
            for l in self.find(input[:i]):
                for r in self.find(input[i + 1:]):
                    root = TreeNode(input[i])
                    root.left = l
                    root.right = r
                    result.append(root)
        return result
print(Solution().generateTrees(3))