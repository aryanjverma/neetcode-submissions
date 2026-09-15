class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        small = min(m, n) - 1
        big = m + n - 2
        answer = 1
        for i in range(small):
            answer *= (big - i) 
            answer /= (small - i)
        return round(answer)