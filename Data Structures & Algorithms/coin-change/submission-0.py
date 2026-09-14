class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [-1] * (amount + 1)
        for i in range(1, amount + 1):
            minNum = -1
            for coin in coins:
                if coin == i:
                    minNum = 1
                    break
                else:
                    if (i - coin) >= 0 and dp[i - coin] != -1:
                        if minNum == -1:
                            minNum = dp[i - coin] + 1
                        else:
                            minNum = min(minNum, dp[i - coin] + 1)
            dp[i] = minNum
        
        return dp[-1]