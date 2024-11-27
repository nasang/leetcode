import graph.UnionFind as UnionFind

class KruskalMST:
    """
    n: n vertices indexed from 0 to n - 1
    edges: edges[i] = [ui, vi, wi], vertex ui and vertex vi connected with egde weighing wi
    """
    def __init__(self, edges, n):
        self.n = n
        self.edges = sorted(edges, key=lambda x: x[2])
    
    def kruskal(self):
        uf = UnionFind(self.n)
        mst_sum = 0
        mst_edge_count = 0
        for u, v, w in self.edges:
            if uf.union(u, v):
                mst_sum  += w
                mst_edge_count += 1
            if mst_edge_count == self.n - 1:
                return mst_sum
        return -1

    