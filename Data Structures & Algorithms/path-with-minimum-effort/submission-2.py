import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        q = [(0, 0, 0)]
        deltas = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        vals = {}
        while q:
            effort, x, y = heapq.heappop(q)
            if (x, y) not in vals or vals[(x, y)] > effort:
                vals[(x, y)] = effort
                if x == n - 1 and y == m - 1:
                    continue
                curr = heights[x][y]
                for dx, dy in deltas:
                    
                    if x + dx >= 0 and x + dx < n and y + dy >= 0 and y + dy < m:
                        heapq.heappush(q, (max(effort, abs(curr - heights[x + dx][y + dy])), x + dx, y + dy))
        return vals[(n - 1, m - 1)]