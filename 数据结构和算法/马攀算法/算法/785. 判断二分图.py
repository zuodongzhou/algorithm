class Solution(object):

    def __init__(self):
        self.dic = {}

    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        for i in range(len(graph)):
            if i not in self.dic :
                if not self.find(graph,i,1):
                    return False
        return True
    def find(self,graph,i,cur):
        for z in graph[i]:
            if z not in self.dic:
                self.dic[z] = -cur
                if not self.find(graph,z,-cur):
                    return False
            else:
                if self.dic[z] == cur:
                    return False
        return True

print(Solution().isBipartite([[1],[0,3],[3],[1,2]]))




