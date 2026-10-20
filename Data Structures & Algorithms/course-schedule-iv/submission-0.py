from collections import deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        for pr in prerequisites:
            a, b = pr
            graph[b].append(a)
        
        def bfs(a, b):
            q = deque()
            visited = set()

            q.append(b)
            visited.add(b)
            
            while q:
                node = q.popleft()
                if node == a:
                    return True
                for pr in graph[node]:
                    if pr not in visited:
                        q.append(pr)
                        visited.add(pr)
            return False
        
        answer = [False] * len(queries)
        
        for i in range(len(queries)):
            a, b = queries[i]
            answer[i] = bfs(a, b)
        return answer
