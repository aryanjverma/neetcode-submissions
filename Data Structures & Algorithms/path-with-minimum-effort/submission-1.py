import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        q = [(0, heights[0][0], 0, 0)]
        deltas = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        vals = {}
        while q:
            effort, prev, x, y = heapq.heappop(q)
            if x >= 0 and x < n and y >= 0 and y < m:
                curr = heights[x][y]
                effort = max(effort, abs(prev - curr))
                if (x, y) not in vals or vals[(x,y)] > effort:
                    vals[(x, y)] = effort
                    for dx, dy in deltas:
                        heapq.heappush(q, (effort, curr, x + dx, y + dy))
        return vals[(n - 1, m - 1)]