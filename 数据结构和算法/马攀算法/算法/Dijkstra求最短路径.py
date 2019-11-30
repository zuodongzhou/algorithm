
#邻接矩阵
class solution:
    def __init__(self):
        self.dic = {}
    def Dijkstra(self,edges):
# edges表示邻接矩阵
        dis = {}
        for i,num in enumerate(edges[0]):
            if num != 0:
                dis[i] = num
        self.dic[0] = 0
        while dis:
            sort_dis = sorted(dis.items(), key= lambda item: item[1])
            #print(sort_dis)
            for k,v in sort_dis:
                if k in self.dic:
                    del dis[k]
                else:
                    self.dic[k] = v
                    del dis[k]
                    cur = v
                    for i, num in enumerate(edges[k]):
                        if num != 0:
                            if i not in self.dic:
                                if i in dis:
                                    dis[i] = min(num+cur,dis[i])
                                else:
                                    dis[i] = num+cur
                    break
        print(self.dic)
edges = [[0, 1, 12, 0, 0, 0],
         [0, 0, 9, 3, 0, 0],
         [0, 0, 0, 0, 5, 0],
         [0, 0, 4, 0, 13, 15],
         [0, 0, 0, 0, 0, 4],
         [0, 0, 0,0, 0, 0]]
solution().Dijkstra(edges)
# 2、使用邻接表
class solution:
    def __init__(self):
        self.dic = {}
    def Dijkstra(self,adj):
# edges表示邻接矩阵
        dis = adj[1]
        self.dic[1] = 0
        while dis:
            sort_dis = sorted(dis.items(), key= lambda item: item[1])
            #print(sort_dis)
            for k,v in sort_dis:
                if k in self.dic:
                    del dis[k]
                else:
                    self.dic[k] = v
                    del dis[k]
                    cur = v
                    if k in adj.keys():
                        for i,num in adj[k].items():
                            if i not in self.dic:
                                if i in dis:
                                    dis[i] = min(num+cur,dis[i])
                                else:
                                    dis[i] = num+cur
                    break
        print(self.dic)
adj = {1: {2: 1, 3: 12}, 2: {4: 3, 3: 9}, 3: {5: 5}, 4: {3: 4, 5: 13, 6: 15}, 5: {6: 4}}
solution().Dijkstra(adj)