import heapq
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        q = [0] * (len(cost) + 1)
        

        for i in range(2, len(cost) + 1):
            q[i] = min(q[i - 1] + cost[i - 1], q[i - 2] + cost[i - 2])
            
        return q[-1]
        
        
