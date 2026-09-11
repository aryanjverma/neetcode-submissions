# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root in self.cache:
            return self.cache[root]
        if not root:
            return 0
        self.cache[root] = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return self.cache[root]
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:        
        if not root:
            return 0    
        self.cache = {}
        return self.helper(root) - 1
    
    def helper(self, root):
        if not root:
            return 0
        return max(max(1 + self.maxDepth(root.left) + self.maxDepth(root.right), self.helper(root.left)), self.helper(root.right))
