# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.cache = {}
        
        def dfs(root):
            
            if not root:
                return 0
            if root in self.cache:
                return self.cache[root]
            left = dfs(root.left)
            right = dfs(root.right)
            if left == -1 or right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            self.cache[root] = 1 + max(left, right)
            return self.cache[root]
        return dfs(root) != -1
