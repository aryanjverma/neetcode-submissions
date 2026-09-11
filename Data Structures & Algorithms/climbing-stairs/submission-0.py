class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        
        tail1 = 2
        tail2 = 1

        for i in range(n - 2):
            tail1 += tail2
            tail2 = tail1 - tail2
        return tail1 