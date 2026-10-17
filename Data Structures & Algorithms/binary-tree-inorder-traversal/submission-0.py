# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def helper(curr):
            if curr:
                helper(curr.left)
                answer.append(curr.val)
                helper(curr.right)
        helper(root)
        return answer