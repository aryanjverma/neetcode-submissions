from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()
        for i in range(len(board[0])):
            if board[0][i] == "O":
                q.append((0, i))
            if board[len(board) - 1][i] == "O":
                q.append((len(board) - 1, i))
        for j in range(1, len(board) - 1):
            if board[j][0] == "O":
                q.append((j, 0))
            if board[j][len(board[0]) - 1] == "O":
                q.append((j, len(board[0]) - 1))
        safe = set()
        def appendQ(x, y):
            if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]) and board[x][y] == "O":
                q.append((x, y))
        while q:
            popped = q.popleft()
            if popped not in safe:
                safe.add(popped)
                x, y = popped
                appendQ(x + 1, y)
                appendQ(x - 1, y)
                appendQ(x, y + 1)
                appendQ(x, y - 1)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in safe:
                    board[i][j] = "X"
        
