from collections import deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for i in range(len(equations)):
            x, y = equations[i]
            value = values[i]
            if x not in graph:
                graph[x] = []
            if y not in graph:
                graph[y] = []
            graph[x].append((y, value))
            graph[y].append((x, 1 / value))
        visited = set()
        def dfs(start, end):
            if start in visited:
                return - 1
            if start == end:
                return 1
            visited.add(start)
            for elem in graph[start]:
                neighbor, value = elem
                a = dfs(neighbor, end)
                if a != - 1:
                    return a * value
            return -1
        answer = []
        for query in queries:
            x, y = query
            if x not in graph or y not in graph:
                answer.append(-1.0)
            else:
                visited = set()
                answer.append(dfs(x, y))
        return answer