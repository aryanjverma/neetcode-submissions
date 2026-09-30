class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacent = [[] for _ in range(n)]
        for edge in edges:
            adjacent[edge[0]].append(edge[1])
            adjacent[edge[1]].append(edge[0])
        visited = set()
        def helper(index):
            if index not in visited:
                visited.add(index)
                if len(adjacent[index]) > 0:
                    for neighbor in adjacent[index]:
                        helper(neighbor)
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                helper(i)
        
        return count