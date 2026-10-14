class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        def helper(l, r):
            if l == r:
                return piles[l]
            if (l, r) in dp:
                return dp[(l, r)]
            answer = piles[l] - helper(l + 1, r)
            answer = max(answer, piles[r] - helper(l, r - 1))
            dp[(l, r)] = answer
            return answer
        return helper(0, len(piles) - 1) > 0
