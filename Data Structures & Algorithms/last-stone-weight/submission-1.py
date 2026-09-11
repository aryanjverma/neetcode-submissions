import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= - 1
        heapq.heapify(stones)
        while len(stones) > 1:
            
            first = abs(heapq.heappop(stones) - heapq.heappop(stones))
            if first != 0:
                heapq.heappush(stones, -1 * first)
        if len(stones) == 0:
            return 0
        return -1 * stones[0]