class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.front = None
        self.back = None
        self.nodeMap = dict()
        self.size = 0
        self.capacity = capacity
    def printList(self):
        phrase = ""
        temp = self.front
        while temp:
            phrase += str(temp.val)
            phrase += ","
            temp = temp.next
        print(phrase)
    def updateList(self) -> None:
        self.nodeMap.pop(self.back.key)
        self.back = self.back.prev
        self.back.next = None
        self.size -= 1
        
    def removeOldNode(self, key):
        
        oldNode = self.nodeMap[key]
        value = oldNode.val
        if self.size == 1:
            self.front = None
            self.back = None
        elif self.size == 2:
            if oldNode == self.front:
                self.front = self.back
                self.back.prev = None
            else:
                self.back = self.front
                self.front.next = None
        elif oldNode.next:
            oldNode.next.prev = oldNode.prev
            if oldNode.prev:
                oldNode.prev.next = oldNode.next
            else:
                self.front = oldNode.next
                if self.front:
                    self.front.prev = None
        else:
            self.back = oldNode.prev
            
            if self.back:
                self.back.next = None
        
        self.size -= 1
        return value
    def addNode(self, key, value):
        temp = self.front
        self.front = ListNode(key=key, val=value)
        if self.size == 0:
            self.back = self.front
        else:
            temp.prev = self.front
            self.front.next = temp
        self.nodeMap[key] = self.front
        self.size += 1
    def get(self, key: int) -> int:
        
        answer = -1
        if key in self.nodeMap:
            val = self.removeOldNode(key)
            self.addNode(key, val)
            answer = self.nodeMap[key].val
        
        return answer
    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            self.removeOldNode(key)
        
        self.addNode(key, value)

        if self.size > self.capacity:
            self.updateList()
    