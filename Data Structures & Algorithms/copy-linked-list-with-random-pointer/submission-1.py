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
        while temp:
            curr.next = Node(x = temp.val)
            nodeMap[temp] = curr.next
            curr = curr.next
            temp = temp.next
        
        curr = new.next
        temp = head
        while temp:
            if temp.random:
                curr.random = nodeMap[temp.random]
            curr = curr.next
            temp = temp.next
        return new.next