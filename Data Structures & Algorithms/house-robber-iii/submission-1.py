# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {}
        def dfs(root):
            if not root:
                return 0
            if root in dp:
                return dp[root]
            skip = 0
            select = 0
            if root.left:
                if root.left.left:
                    select += dfs(root.left.left)
                if root.left.right:
                    select += dfs(root.left.right)
                skip += dfs(root.left)
            if root.right:
                if root.right.left:
                    select += dfs(root.right.left)
                if root.right.right:
                    select += dfs(root.right.right)
                skip += dfs(root.right)
            dp[root] = max(skip, select + root.val)
            return dp[root]
        return dfs(root)