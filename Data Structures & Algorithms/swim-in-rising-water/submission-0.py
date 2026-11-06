import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = [(grid[0][0], 0, 0)]
        startVisited = {}
        while q:
            
            time, x, y = heapq.heappop(q)
            if x == n - 1 and y == n - 1:
                return time
            if not (x, y) in startVisited or time < startVisited[(x, y)]:
                startVisited[(x, y)] = time
                for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    nx = x + dx
                    ny = y + dy
                    if nx >= 0 and nx < n and ny >= 0 and ny < n:
                        heapq.heappush(q, (max(time, grid[nx][ny]), nx, ny))
        return - 1