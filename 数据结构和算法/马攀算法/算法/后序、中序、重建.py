class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if tin == []:
            return None
        root = TreeNode(pre[-1])
        cur = tin.index(pre[-1])
        root.left = self.reConstructBinaryTree(pre[0:cur], tin[0:cur])
        root.right = self.reConstructBinaryTree(pre[cur:-1], tin[cur + 1:])
        return root

    def find(self, pre, tin):
        root = self.reConstructBinaryTree(pre, tin)
        self.result = []
        self.pre(root)
        return self.result

    def pre(self, root):
        if root == None:
            return
        self.result.append(root.val)
        if root.left:
            self.pre(root.left)
        if root.right:
            self.pre(root.right)


tin = list('dgbaechf')
pre = list('gbdehfca')
print(Solution().find(pre, tin))