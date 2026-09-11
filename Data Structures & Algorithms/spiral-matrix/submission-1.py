class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = [(0,1), (1,0), (0,-1),(-1,0)]
        answer = []
        m = len(matrix)
        n = len(matrix[0])
        i = 0 
        j = 0
        d = 0
        while len(answer) < m * n:
            answer.append(matrix[i][j])
            matrix[i][j] = None

            ni = i + direction[d][0]
            nj = j + direction[d][1]
            if ni < 0 or ni >= m or nj <0 or nj >= n or matrix[ni][nj] is None:
                d += 1
                d %=4
            i += direction[d][0]
            j += direction[d][1]
        return answer