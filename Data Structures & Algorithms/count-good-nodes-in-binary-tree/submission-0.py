# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodNodes = 0

        def dfs(root, minNumber):
            if root:
                if root.val >= minNumber:
                    self.goodNodes += 1
                dfs(root.left, max(minNumber, root.val))
                dfs(root.right, max(minNumber, root.val))
        dfs(root, float('-inf'))
        return self.goodNodes