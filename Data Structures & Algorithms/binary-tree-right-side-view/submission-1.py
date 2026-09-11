# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        q = deque()
        if root:
            q.append(root)
        while q:
            

            first = q.popleft()
            length = len(q)
            answer.append(first.val)
            if first.right:
                q.append(first.right)
            if first.left:
                q.append(first.left)
            

            for _ in range(length):
                popped = q.popleft()
                if popped.right:
                    q.append(popped.right)
                if popped.left:
                    q.append(popped.left)
        return answer