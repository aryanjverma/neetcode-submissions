"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        nodeGraph = dict()
        root = Node(val = node.val, neighbors = node.neighbors.copy())
        nodeGraph[node] = root
        q = deque()
        q.append(root)
        while q:
            currNode = q.popleft()
            for i in range(len(currNode.neighbors)):
                neighbor = currNode.neighbors[i]
                
                if neighbor not in nodeGraph:
                    
                    newNode = Node(val = neighbor.val, neighbors = neighbor.neighbors.copy())
                    nodeGraph[neighbor] = newNode
                    currNode.neighbors[i] = newNode
                    q.append(newNode)
                else:
                    
                    currNode.neighbors[i] = nodeGraph[neighbor]
        return root