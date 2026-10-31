from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        edgeCount = [0] * n
        leaves = deque()
        for i in range(n):
            edgeCount[i] = len(graph[i])
            if edgeCount[i] == 1:
                leaves.append(i)
        
        while leaves:
            if n <= 2:
                return list(leaves)
            numLeaves = len(leaves)
            
            for _ in range(numLeaves):
                node = leaves.popleft()
                n -= 1
                for neighbor in graph[node]:
                    edgeCount[neighbor] -= 1
                    if edgeCount[neighbor] == 1:
                        leaves.append(neighbor)
        return []