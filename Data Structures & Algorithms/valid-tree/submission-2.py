from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        kids = [[] for _ in range(n)]
        for edge in edges:
            a, b = edge
            kids[a].append(b)
            kids[b].append(a)
        visited = [0] * n
        q = deque()
        q.append(0)
        while q:
            popped = q.popleft()
            if visited[popped] == 1:
                return False
            visited[popped] = 1
            for kid in kids[popped]:
                kids[kid].remove(popped)
                q.append(kid)
                
        return sum(visited) == n