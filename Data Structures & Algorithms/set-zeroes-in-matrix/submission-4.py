class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        firstCol = 1
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j == 0:
                        firstCol = 0
                    else:
                        matrix[0][j] = 0
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0:
                    matrix[i][j] = 0
                elif j == 0 and firstCol == 0:
                    matrix[i][j] = 0
                elif matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        
        if matrix[0][0] == 0:
            matrix[0] = [0] * len(matrix[0])
        if firstCol == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        