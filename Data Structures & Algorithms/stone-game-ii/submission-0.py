class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}
        def helper(i, m):
            if i >= len(piles):
                return 0
            if (i, m) in dp:
                return dp[(i, m)]
            answer = float('-inf')
            s = 0
            for x in range(1, 2 * m + 1):
                if i + x - 1 >= len(piles):
                    break
                s += piles[i + x - 1]
                l = s - helper(i + x, max(m, x))
                answer = max(answer, l)
            dp[(i, m)] = answer
            return answer
        
        
        answer = helper(0, 1)
        
        return (answer + sum(piles)) // 2