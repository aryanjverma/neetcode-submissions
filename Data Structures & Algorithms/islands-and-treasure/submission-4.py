from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        q = deque()   
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))
        def updateQ(x, y):
            if x + 1 < len(grid):
                if grid[x + 1][y] == INF:
                    grid[x + 1][y] = grid[x][y] + 1
                    q.append((x + 1, y))
            if x - 1 >= 0:
                if grid[x - 1][y] == INF:
                    grid[x - 1][y] = min(grid[x - 1][y], grid[x][y] + 1)
                    q.append((x - 1, y))
            if y + 1 < len(grid[0]):
                if grid[x][y + 1] == INF:
                    grid[x][y + 1] = grid[x][y] + 1
                    q.append((x, y + 1))
            if y - 1 >= 0:
                if grid[x][y - 1] == INF:
                    grid[x][y - 1] = grid[x][y] + 1
                    q.append((x, y - 1))

        while q:
            x, y = q.popleft()
            updateQ(x, y)
