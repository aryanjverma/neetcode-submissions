from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshFruits = set()
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    freshFruits.add((i, j))
                elif grid[i][j] == 2:
                    q.append((i, j))
        count = 0
        
        while len(freshFruits) != 0 and q:
            count += 1
            length = len(q)
            for i in range(length):
                x, y = q.popleft()
                if (x + 1, y) in freshFruits:
                    q.append((x + 1, y))
                    freshFruits.remove((x + 1, y))
                if (x - 1, y) in freshFruits:
                    q.append((x - 1, y))
                    freshFruits.remove((x - 1, y))
                if (x, y + 1) in freshFruits:
                    q.append((x, y + 1))
                    freshFruits.remove((x, y + 1))
                if (x, y - 1) in freshFruits:
                    q.append((x, y - 1))
                    freshFruits.remove((x, y - 1))
        if len(freshFruits) > 0:
            return -1
        return count