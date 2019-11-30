graph = {'A':['B','C'],
            'B':['A','C','D'],
            'C':['A','B','D','E'],
            'D':['B','C','E','F'],
          'E':['C','D'],
          'F':["D"]
          }
class solution:
    def BFS(self,graph,start):
        queue = [start]
        seen =set()
        seen.add(start)
        result = []
        while queue:
            cur_node = queue.pop(0)
            result.append(cur_node)
            for node in graph[cur_node]:
                if node not in seen:
                    queue.append(node)
                    seen.add(node)
        return result
    def DFS(self,graph,start):
        stack = [start]
        seen = set()
        seen.add(start)
        result = []
        while stack:
            cur_node =stack.pop()
            result.append(cur_node)
            for node in graph[cur_node]:
                if node not in seen:
                    stack.append(node)
                    seen.add(node)
        return result

print(solution().DFS(graph,'E'))
print(solution().BFS(graph,'A'))
