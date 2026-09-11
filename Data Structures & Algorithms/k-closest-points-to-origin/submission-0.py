import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        q = []

        for point in points:
            heapq.heappush(q, (-1 * point[0] * point[0] + -1 * point[1] * point[1], point))
            if len(q) > k:
                heapq.heappop(q)
        
        for i in range(len(q)):
            q[i] = q[i][1]
        return q