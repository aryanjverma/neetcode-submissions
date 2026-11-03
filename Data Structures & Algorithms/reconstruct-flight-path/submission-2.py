import heapq
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for a, b in tickets:
            heapq.heappush(graph[a], b)
        answer = []
        def dfs(node):
            while graph[node]:
                dfs(heapq.heappop(graph[node]))
            answer.append(node)
        dfs("JFK")
        return answer[::-1]