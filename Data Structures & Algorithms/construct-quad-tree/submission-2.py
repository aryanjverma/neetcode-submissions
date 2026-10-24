"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def recurse(x, y, length):
            val = (grid[x][y]) == 1
            if length == 1:
                return Node(val=val, isLeaf=True)
            else:
                newLength = length // 2
                child1 = recurse(x, y, newLength)
                child2 = recurse(x, y + newLength, newLength)
                child3 = recurse(x + newLength, y, newLength)
                child4 = recurse(x + newLength, y + newLength, newLength)
                
                if child1.isLeaf and child2.isLeaf and child3.isLeaf and child4.isLeaf and child1.val == child2.val  and child3.val == child4.val and child1.val == child3.val:
                    return Node(val=val,isLeaf=True)
                else:
                    return Node(val=val,isLeaf=False, topLeft=child1, topRight=child2, bottomLeft=child3, bottomRight=child4)
        return recurse(0, 0, len(grid))