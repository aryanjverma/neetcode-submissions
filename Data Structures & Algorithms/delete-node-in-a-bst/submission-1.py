# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            if root.left is None:
                return root.right
            elif root.left.right is None:
                root.left.right = root.right
                return root.left
            else:
                temp = root.left
                while temp.right.right:
                    temp = temp.right
                newRoot = temp.right
                temp.right = temp.right.left
                newRoot.right = root.right
                newRoot.left = root.left
                return newRoot
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        return root