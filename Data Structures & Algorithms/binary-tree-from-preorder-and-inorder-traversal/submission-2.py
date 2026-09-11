# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.nodeMap = dict()
        for index, num in enumerate(inorder):
            self.nodeMap[num] = index
        self.preorder = preorder
        self.pIdx = 0
        def helper(iLeft, iRight):
            if iLeft > iRight or self.pIdx >= len(self.preorder):
                return None
            root = TreeNode(val=self.preorder[self.pIdx])
            mid = self.nodeMap[self.preorder[self.pIdx]]
            self.pIdx += 1
            
        
            root.left = helper(iLeft, mid - 1)
            root.right = helper(mid + 1, iRight)
            return root
        return helper(0, len(preorder))