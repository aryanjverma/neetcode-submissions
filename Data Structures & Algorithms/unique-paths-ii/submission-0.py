class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1] * n for _ in range(m)]
        dp[0][0] = 1
        def helper(i, j):
            if i < 0 or j < 0 or obstacleGrid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            if dp[i][j] != - 1:
                return dp[i][j]
            down = helper(i - 1,j)
            left = helper(i, j - 1)
            
            dp[i][j] = down + left

            return down + left
        a = helper(m - 1, n - 1)
        print(dp)
        return a