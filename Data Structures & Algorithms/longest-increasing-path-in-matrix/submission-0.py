class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}
        def dfs(i, j, m):
            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] <= m:
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            m = max(m, matrix[i][j])
            answer = 1 + max(max(dfs(i + 1, j, m), dfs(i - 1, j, m)), max(dfs(i, j + 1, m), dfs(i, j - 1, m)))
            cache[(i, j)] = answer
            return answer
        answer = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                answer = max(answer, dfs(i, j, float('-inf')))
        
        return answer