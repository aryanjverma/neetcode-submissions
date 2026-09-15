class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.size = 0
        def dfs(x, y):
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] == 1:
                self.size += 1
                grid[x][y] = 2
                dfs(x, y + 1)
                dfs(x, y - 1)
                dfs(x - 1, y)
                dfs(x + 1, y)
        
        maxSize = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.size = 0
                    dfs(i, j)
                    maxSize = max(maxSize, self.size)
        
        return maxSize