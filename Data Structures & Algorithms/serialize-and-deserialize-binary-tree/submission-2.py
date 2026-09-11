# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        answer = []
        
        q = deque()
        q.append(root)
        while q:
            popped = q.popleft()
            if popped:
                answer.append(chr(popped.val // 256))
                answer.append(chr(popped.val % 256))
                q.append(popped.left)
                q.append(popped.right)
            else:
                answer.append(chr(255))
                answer.append(chr(255))
        
        while answer and answer[-1] == chr(255):
            answer.pop()

        return ''.join(answer)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return None
        nodes = []
        
        for i in range(len(data) // 2):
            firstByte = ord(data[2 * i])
            if firstByte == 255:
                nodes.append(None)
            else:
                secondByte = ord(data[2 * i + 1])
                number = firstByte * 256 + secondByte
                nodes.append(TreeNode(val=number))
        q = deque()
        q.append(0)
        index = 1
        while index < len(nodes) and q:
            currIndex = q.popleft()
            if index < len(nodes) and nodes[index]:
                nodes[currIndex].left = nodes[index]
                q.append(index)
            index += 1
            if index < len(nodes) and nodes[index]:
                nodes[currIndex].right = nodes[index]
                q.append(index)    
            index += 1  

        return nodes[0]