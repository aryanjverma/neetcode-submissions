class DSU:
    def __init__(self, n):
        self.rep = list(range(n))
        self.rank = [1] * n
    def find(self, node):
        curr = node
        while curr != self.rep[curr]:
            self.rep[curr] = self.rep[self.rep[curr]]
            curr = self.rep[curr]
        return curr
    def union(self, u, v):
        u -= 1
        v -= 1
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] > self.rank[pv]:
            pu, pv = pv, pu
        self.rep[pu] = pv
        self.rank[pv] += self.rank[pu]
        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        for edge in edges:
            if not dsu.union(edge[0], edge[1]):
                return edge
