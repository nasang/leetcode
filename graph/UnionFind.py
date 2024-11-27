class UnionFind():
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return u
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        self.parent[pu] = pv
        return True
