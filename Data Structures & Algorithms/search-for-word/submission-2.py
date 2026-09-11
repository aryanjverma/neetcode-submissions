class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        def helper(word, position):
            
            if len(word) == 0:
                return True
            x = position[0]
            y = position[1]
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                return False
            if board[x][y] != word[0]:
                return False
            word = word[1:]
            temp = board[x][y]
            board[x][y] = "0"
            answer = helper(word, (x + 1, y)) or helper(word, (x - 1, y)) or helper(word, (x, y - 1)) or helper(word, (x, y + 1))
            board[x][y] = temp
            return answer
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(word, (i, j)):
                    return True
        return False

        