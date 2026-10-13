import heapq
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        q = [(0, (0, 0))]
        visited = dict()
        while q:
            score, position = heapq.heappop(q)
            x, y = position
            if x < m and y < n and (position not in visited or visited[(x, y)] > score + grid[x][y]):
                visited[(x, y)] = score + grid[x][y]
                heapq.heappush(q, (visited[(x, y)], (x, y + 1)))
                heapq.heappush(q, (visited[(x, y)], (x + 1, y)))
        return visited[(m - 1, n - 1)]