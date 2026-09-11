class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.children = dict()
        self.isWord = False
    def addChild(self, child):
        if not self.hasChild(child):
            self.children[child] = TreeNode(val=child)
    def hasChild(self, child):
        return child in self.children
    def getChild(self, child):
        if not self.hasChild(child):
            return None
        return self.children[child]
    def becomeWord(self):
        self.isWord = True
class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        temp = self.root
        for char in word:
            temp.addChild(char)
            temp = temp.getChild(char)
        temp.becomeWord()
    def search(self, word: str) -> bool:
        temp = self.root
        for char in word:
            temp = temp.getChild(char)
            if temp is None:
                return False
        return temp.isWord

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for char in prefix:
            temp = temp.getChild(char)
            if temp is None:
                return False
        return True