class Solution(object):
    def __init__(self):
        self.max_count = 0
    def maxAreaOfIsland(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.boom(i,j,grid,0)
        return self.max_count
    def boom(self,i,j,grid,count):
        if 0 <= i <= len(grid)-1 and 0 <= j <= len(grid[0])-1:
            if grid[i][j] == 0:
                return count
            else:
                count += 1
                if count > self.max_count:
                    self.max_count = count
                grid[i][j] = 0
                count = self.boom(i-1,j,grid,count)
                count = self.boom(i+1,j,grid,count)
                count = self.boom(i,j-1,grid,count)
                count = self.boom(i,j+1,grid,count)
                return count
        else:
            return count
print(Solution().maxAreaOfIsland([[1,1],[1,0]]))