class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def helper(amount, index):
            if amount < 0 or index >= len(coins):
                return 0
            if (amount, index) in dp:
                return dp[amount, index]
            if amount == 0:
                return 1
            answer = helper(amount - coins[index], index) + helper(amount, index + 1)
            dp[(amount, index)] = answer
            return answer

        return helper(amount, 0)        
