'''
输入:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
输出: 2
说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
第2个学生自己在一个朋友圈。所以返回2。
'''
class Solution:
    def findCircleNum(self, M):
        n = len(M)
        circles = {i: i for i in range(n)}

        for i in range(n):
            for j in range(i + 1, n):
                if M[i][j] == 1:
                    circles[self.find(circles,i)] = self.find(circles,j)
        return sum([1 for k, v in circles.items() if k == v])
    def find(self,circles,i):
        while i != circles[i]:
            i = circles[i]
        return i

class solution:
    def __init__(self):
        self.dic = {}
    def test(self,edges):
        self.BCJ(edges)
        result = {}
        for k, v in self.dic.items():
            if v not in result:
                result[v] = []
            result[v].append(k)
        print(result)
        print(self.dic)
    def BCJ(self,edges):
        for line in edges:
            new_node = []
            old_node = []
            for num in line:
                if num not in self.dic:
                    new_node.append(num)
                else:
                    old_node.append(num)
            root = self.combine(old_node)
            if root:
                for node in new_node:
                    self.dic[node] = root
            else:
                if  new_node:
                    root = new_node[0]
                    for node in new_node:
                        self.dic[node] = root
    def combine(self,old_node):
        if not old_node:
            return None
        else:
            root = self.find(old_node[0])
            for node in old_node[1:]:
                self.dic[self.find(node)] = root
            return root
    def find(self,node):
        while node != self.dic[node]:
            node = self.dic[node]
        return node
edges = [['a','b','c'],['f','r','g','a'],['y','i','p']]
print(solution().BCJ(edges))

















