from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        q = deque()
        for i in range(len(heights[0])):
            q.append((0, i))
            
        for i in range(1, len(heights)):
            q.append((i, 0))
        pacific = set()
        def qAppend(i, j, num):
            if i >= 0 and i < len(heights) and j >= 0 and j < len(heights[0]) and heights[i][j] >= num:
                q.append((i, j))
            
        while q:
            x, y = q.popleft()
            if (x, y) not in pacific:
                pacific.add((x, y))
                qAppend(x + 1, y, heights[x][y])
                qAppend(x - 1, y, heights[x][y])
                qAppend(x, y + 1, heights[x][y])
                qAppend(x, y - 1, heights[x][y])
        
        
        for i in range(len(heights[0])):
            q.append((len(heights) - 1, i))
            
        for i in range(len(heights) - 1):
            q.append((i, len(heights[0]) - 1))
        atlantic = set()
        
        while q:
            x, y = q.popleft()
            if (x, y) not in atlantic:
                atlantic.add((x, y))
                qAppend(x + 1, y, heights[x][y])
                qAppend(x - 1, y, heights[x][y])
                qAppend(x, y + 1, heights[x][y])
                qAppend(x, y - 1, heights[x][y])
        answer = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in pacific and (i, j) in atlantic:
                    answer.append((i, j))
        
        return answer