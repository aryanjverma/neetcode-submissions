from collections import deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        for pr in prerequisites:
            a, b = pr
            graph[a].append(b)
        
        from functools import cache
        @cache 
        def dfs(a, b):
            if a == b:
                return True
            
            for pr in graph[a]:
                if dfs(pr, b):
                    return True       
            return False
        
        answer = [False] * len(queries)

        for i in range(len(queries)):
            a, b = queries[i]
            answer[i] = dfs(a, b)
        return answer
