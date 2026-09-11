import heapq
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        q = [0] * (len(cost) + 1)
        q[0] = cost[0]
        q[1] = cost[1]

        for i in range(2, len(cost) + 1):
            q[i] = min(q[i - 1], q[i - 2])
            if i != len(cost):
                q[i] += cost[i]
        return q[-1]
        
        
