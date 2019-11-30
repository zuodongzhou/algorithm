class TreeNode(object):

    def __init__(self, x=None, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
#前序遍历（递归）
class Solution(object):

    def __init__(self):  # 用一个类属性(类似于全局变量)来保存需要返回遍历列表
        self.result = []

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []  # return后不能为空，必须加[]，由于函数最后一行是self.result，最终会返回它的值，且碰到子树叶子节点返回上i层后，后面还有代码，所以不影响叶子节点？
        self.result.append(root.val)
        self.preorderTraversal(root.left)  # 调用class内部方法时，self不用传值，故括号内不用写self
        self.preorderTraversal(root.right)
        return self.result  # self.result or result? 每次return的值都会被下次return的值覆盖
#前序遍历（非递归）
class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        stack = [root]  # 栈顶先入栈
        result = []
        while stack:  # 循环条件为栈不为空
            cur = stack.pop()  # 栈顶出栈，再看看下一个出栈是左子树
            result.append(cur.val)  #每次记录一个
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return result
#中序遍历（递归）
class Solution(object):

    def __init__(self):  # 用一个类属性(类似于全局变量)来保存需要返回遍历列表
        self.result = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.inorderTraversal(root.left)
        self.result.append(root.val)
        self.inorderTraversal(root.right)
        return self.result
#中序遍历（非递归）
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        # 1. 根节点先入栈
        stack = [root]
        cur = root
        while stack:
            # 2. 中序遍历要求先访问左子树，因此一路访问左子树，直到None
            while cur:
                cur = cur.left
                if cur:
                    stack.append(cur)
            # 左子树全部遍历完了之后，栈顶出栈(返回上一层，遍历上一层的右子树)
            root = stack.pop()
            result.append(root.val)
            # 右子树入栈，再让右子树的左子树入栈(root.right赋给cur，就能直接返回上层cur的循环，直接访问左子树)
            if root.right:
                cur = root.right
                stack.append(cur)
        return result

#后序遍历（递归）
class Solution(object):

    def __init__(self):  # 用一个类属性(类似于全局变量)来保存需要返回遍历列表
        self.result = []
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.result.append(root.val)
        return self.result
#后序遍历（非递归）
class Solution(object):
    def postorderTraverse(self,root):
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            root = stack.pop()
            result.append(root.val)#依次记录栈1弹出的
            if root.left :
                stack.append(root.left)
            if root.right :
                stack.append(root.right)
        return result[::-1]


