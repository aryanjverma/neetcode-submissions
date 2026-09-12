class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        
        path = []
        
        cols = set()
        negDiags = set()
        posDiags = set()
        def helper(row):
            if row == n:
                board = []
                for col in path:
                    row = ['.'] * n
                    row[col] = 'Q'
                    board.append(''.join(row))
                solutions.append(board)
                return
            for col in range(n):
                if col in cols or row - col in negDiags or row + col in posDiags:
                    continue
                path.append(col)
                cols.add(col)
                negDiags.add(row - col)
                posDiags.add(row + col)

                helper(row + 1)

                path.pop()
                cols.remove(col)
                negDiags.remove(row - col)
                posDiags.remove(row + col)
        helper(0)
        return solutions