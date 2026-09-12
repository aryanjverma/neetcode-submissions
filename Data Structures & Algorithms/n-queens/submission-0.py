class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queens = []
        self.n = n
        def helper(row, currAnswer):
            if len(currAnswer) > 1:
                newX = row - 1
                newY = currAnswer[-1]
                
                for i in range(len(currAnswer) - 1):
                    x = i
                    y = currAnswer[i]
                    if newX == x or newY == y or newX - newY == x - y or newX + newY == x + y:
                        return
            if row == self.n:
                queens.append(currAnswer)
            else:  
                for i in range(self.n):
                    helper(row + 1, currAnswer + [i])
        helper(0, [])
        answers = []
        
        for queenPair in queens:
            answer = []
            for queen in queenPair:
                row = ['.'] * n
                row[queen] = 'Q'
                answer.append(''.join(row))
            answers.append(answer)
        return answers