import heapq
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for ticket in tickets:
            a, b = ticket
            heapq.heappush(graph[a], b)
        answer = []
        def dfs(node):
            while graph[node]:
                dfs(heapq.heappop(graph[node]))
            answer.append(node)
        dfs("JFK")
        return answer[::-1]