# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.answer = root.val
        def dfs(root):
            left = None
            right = None
            currAnswer = root.val
            if root.left:
                left = dfs(root.left)
                currAnswer = max(currAnswer, root.val + left)
            if root.right:
                right = dfs(root.right)
                currAnswer = max(currAnswer, root.val + right)
            if root.right and root.left:
                self.answer = max(self.answer, (max(currAnswer, root.val + left + right)))
            
            self.answer = max(self.answer, currAnswer) 
            print(f"{root.val}:{currAnswer}")
            return currAnswer
        dfs(root)
        return self.answer