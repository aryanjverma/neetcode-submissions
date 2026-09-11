class TreeNode:
    def __init__(self):
        self.isWord = False
        self.children = dict()

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        temp = self.root
        for char in word:
            if char not in temp.children:
                temp.children[char] = TreeNode()
            temp = temp.children[char]
        temp.isWord = True
    def search(self, word: str) -> bool:
        temp = self.root
        for char in word:
            if char not in temp.children:
                return False
            temp = temp.children[char]
        return temp.isWord

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for char in prefix:
            if char not in temp.children:
                return False
            temp = temp.children[char]
        return True