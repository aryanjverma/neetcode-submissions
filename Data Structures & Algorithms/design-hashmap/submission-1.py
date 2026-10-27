class Node:
    def __init__(self, key, val, n=None):
        self.key = key
        self.val = val
        self.n = n
class MyHashMap:

    def __init__(self):
        self.con = [None] * 100

    def put(self, key: int, value: int) -> None:
        node = self.con[key % 100]
        while node and node.key != key:
            node = node.n
        if node:
            node.val = value
        else:
            self.con[key % 100] = Node(key, value, self.con[key % 100])
    def get(self, key: int) -> int:
        node = self.con[key % 100]
        while node:
            if node.key == key:
                return node.val
            node = node.n
        return - 1

    def remove(self, key: int) -> None:
        curr = self.con[key % 100]
        trail = None
        while curr and curr.n and curr.key != key:
            trail = curr
            curr = curr.n
        if curr and curr.key == key:
            if trail:
                trail.n = curr.n
            else:
                self.con[key % 100] = curr.n

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)