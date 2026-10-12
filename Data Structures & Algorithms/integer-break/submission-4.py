class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n):
            halfWay = i // 2
            
            if i % 2 == 0:
                
                for j in range(halfWay ):
                    dp[i] = max(dp[i], dp[j] * dp[i - j - 1])
                    dp[i] = max(dp[i], (j + 1) * dp[i - j - 1])
                    dp[i] = max(dp[i], dp[j] * (i - j))
                    dp[i] = max(dp[i], (j + 1) * (i - j))   
            else:
                for j in range(halfWay + 1):
                    dp[i] = max(dp[i], dp[j] * dp[i - j - 1])
                    dp[i] = max(dp[i], (j + 1) * dp[i - j - 1])
                    dp[i] = max(dp[i], dp[j] * (i - j))
                    dp[i] = max(dp[i], (j + 1) * (i - j))
        
        return dp[-1]