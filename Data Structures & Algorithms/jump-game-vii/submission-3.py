from collections import deque
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False] * n
        dp[0] = True
        canMove = 0
        for i in range(n):
            if i - minJump >= 0 and dp[i - minJump]:
                canMove += 1
            if i - maxJump >= 0 and dp[i - maxJump - 1]:
                canMove -= 1
            if canMove > 0 and s[i] == '0':
                dp[i] = True
        return dp[-1]