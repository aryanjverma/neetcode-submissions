"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new = Node(x = 0)
        curr = new
        prev = None
        nodeMap = dict()
        temp = head
        while head:
            curr.next = Node(x = head.val)
            nodeMap[head] = curr.next
            if prev:
                prev.next = curr.next
            prev = curr.next
            curr = curr.next
            head = head.next
        
        curr = new.next
        while temp:
            
            if temp.random:
                curr.random = nodeMap[temp.random]
            curr = curr.next
            temp = temp.next
        return new.next