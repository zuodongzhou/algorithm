

'''
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:

输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.


'''
'''
我们可以先不管这个否是二叉树,我们发现,
如果我们选了 cur 这个节点 那么就说明 
我们不能选它的所有子节点(还有父节点)。 
对于每一个节点，都只有选和不选两种情况。
我们每次考虑一棵子树，那么根只有两种情况，
选和不选(我们让dp[0]表示不选,dp[1]表示选)。 
对于选择了根,那么我们就不能选它的儿子了 如果没有选根，
我们就可以任意选了(即选最大的那一个) 然后我们做一次dfs即可

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:

    def dp(self, cur):
        if not cur:
            return [0, 0]  #一个是不要根节点，一个是要
        l = self.dp(cur.left)
        r = self.dp(cur.right)
        return [max(l) + max(r), cur.val + l[0] + r[0]]

    def rob(self, root):
        return max(self.dp(root))




class Solution:
    def __init__(self):
        self.cache = {}
    def rob(self, root) :
        if not root:
            return 0
        ll = self.rob(root.left.left) if root.left else 0
        lr = self.rob(root.left.right) if root.left else 0
        rl = self.rob(root.right.left) if root.right else 0
        rr = self.rob(root.right.right) if root.right else 0
        if root in self.cache:
            return self.cache[root]
        else:
            self.cache[root] = max(root.val + ll +lr + rl+ rr ,self.rob(root.left)+self.rob(root.right))
        return max(root.val + ll +lr + rl+ rr ,self.rob(root.left)+self.rob(root.right))