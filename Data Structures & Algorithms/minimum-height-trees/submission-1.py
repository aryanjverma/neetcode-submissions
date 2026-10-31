import heapq
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for edge in edges:
            a, b = edge
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        def findHeight(node):
            visited.add(node)
            subHeight = 0
            for neighbor in graph[node]:
                if neighbor not in visited:
                    subHeight = max(subHeight, findHeight(neighbor))
            return subHeight + 1
        
        q = []
        for i in range(n):
            visited = set()
            heapq.heappush(q, (findHeight(i), i))
        
        m, node = heapq.heappop(q)
        answer = [node]
        while q and q[0][0] == m:
            height, node = heapq.heappop(q)
            answer.append(node)
        return answer