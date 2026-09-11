class TreeNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        temp = self.root
        for char in word:
            if char not in temp.children:
                temp.children[char] = TreeNode()
            temp = temp.children[char]
        temp.isEnd = True
    def search(self, word: str) -> bool:
        
        return self.searchHelper(word, self.root)
    def searchHelper(self, word, root):
        if len(word) == 0:
            return root.isEnd
        
        temp = root
        for i in range(len(word)):
            char = word[i]
            if char == '.':
                for key in temp.children:
                    if self.searchHelper(word[i + 1:], temp.children[key]):
                        return True
                return False
            if char not in temp.children:
                return False
            temp = temp.children[char]
        return temp.isEnd