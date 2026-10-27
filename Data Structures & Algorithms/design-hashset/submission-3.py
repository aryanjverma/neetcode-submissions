class Node:
    def __init__(self, key, n=None):
        self.key = key
        self.n = n
class MyHashSet:
    def __init__(self):
        self.con = [None] * 100 
    def add(self, key: int) -> None:
        if not self.contains(key):
            self.con[key % 100] = Node(key=key, n=self.con[key % 100])
    def remove(self, key: int) -> None:
        node = self.con[key % 100]
        trail = None
        while node and node.n and node.key != key:
            trail = node
            node = node.n
        if node and node.key == key:
            if trail:
                trail.n = node.n
            else:
                
                self.con[key % 100] = node.n
    def contains(self, key: int) -> bool:
        node = self.con[key % 100]
        while node:
            if node.key == key:
                return True
            node = node.n
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)