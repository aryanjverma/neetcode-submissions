class Trie:
    def __init__(self, index=-1):
        self.children = {}
        self.index = index
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for i in range(len(words)):
            word = words[i]
            temp = root
            for char in word:
                if char not in temp.children:
                    temp.children[char] = Trie()
                temp = temp.children[char]
            temp.index = i
        answer = []
        def discover(x, y, node):
            if node.index != -1:
                answer.append(words[node.index])
                node.index = -1
            if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]):
                if board[x][y] in node.children:
                    c = board[x][y]
                    board[x][y] = "#"
                    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        discover(x + dx, y + dy, node.children[c])
                    board[x][y] = c
        for i in range(len(board)):
            for j in range(len(board[0])):
                discover(i, j, root)
        return answer