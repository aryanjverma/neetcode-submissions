import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for start, end, time in times:
            graph[start - 1].append((end - 1, time))
        times = [-1] * n
        q = [(0, k - 1)]
        while q:      
            time, node = heapq.heappop(q)
            if times[node] == -1:
                times[node] = time
                n -= 1
            else:
                if times[node] > time:
                    times[node] = time
                else:
                    continue
            if n == 0:
                break
            for neighbor, newTime in graph[node]:
                heapq.heappush(q, (time + newTime, neighbor))
        best = 0
        for time in times:
            if time == -1:
                return - 1
            best = max(time, best)
        return best