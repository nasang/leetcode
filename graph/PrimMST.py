from collections import defaultdict
import heapq


class PrimMst:
    """
    n: n vertices indexed from 0 to n - 1
    edges: edges[i] = [ui, vi, wi], vertex ui and vertex vi connected with egde weighing wi
    """
    def __init__(self, edges, n):
        self.n = n
        self.graph = defaultdict(dict)
        for u, v, w in edges:
            self.graph[u][v] = self.graph[v][u] = min(self.graph[u].get(v, float('inf'), w))

    def prim(self, src):
        pq = [(0, src)]
        mst = set()
        mst_sum = 0
        dist_map = {i: float('inf') for i in range(1, self.n)}
        while pq:
            w, u = heapq.heappop(pq)
            if u in mst:
                continue
            mst.add(u)
            mst_sum += w
            if len(mst) == self.n:
                return mst_sum
            for v, new_w in self.graph[u]:
                if v not in mst:
                    if new_w < dist_map[v]:
                        dist_map[v] = new_w
                        heapq.heappush(pq, (new_w, v))
        return -1
