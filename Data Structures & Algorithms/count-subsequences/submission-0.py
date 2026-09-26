class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        dp = {}
        def helper(i, j):
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            answer = 0
            if s[i] == t[j]:
                answer += helper(i + 1, j + 1)            
            answer += helper(i + 1, j)
        
            dp[(i, j)] = answer
            return answer
        answer = helper(0, 0)
        print(dp)
        return answer