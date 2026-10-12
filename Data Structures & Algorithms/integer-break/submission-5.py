class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = i
            if i == n:
                dp[i] = 0
            for j in range(1, i):
                dp[i] = max(dp[i], dp[j] * dp[i - j])
        return dp[-1]