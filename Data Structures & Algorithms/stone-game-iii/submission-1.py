class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {}
        def helper(index):
            if index >= len(stoneValue):
                return 0
            if index in dp:
                return dp[index]
            
            res, total = float("-inf"), 0
            for j in range(index, min(index + 3, len(stoneValue))):
                total += stoneValue[j]
                res = max(res, total - helper(j + 1))
            dp[index] = res
            return res
        answer = helper(0)
        
        if answer > 0:
            return "Alice"
        if answer < 0:
            return "Bob"
        return "Tie"