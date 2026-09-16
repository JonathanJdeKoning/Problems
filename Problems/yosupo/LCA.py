
from collections import defaultdict
class LCA:
    def __init__(self, edges, N, root):
        from math import ceil, log2
        self.N = N
        self.LOG = ceil(log2(self.N))
        self.root = root
        self.E = edges
        # Initialize P with 0 (assuming root's parent is root/0)
        self.P = [[0] * self.LOG for _ in range(self.N)]
        self.D = [0] * self.N
        self.old2New = {}
        self.new2Old = []

    def process(self):
        # 1. Topology & ID Mapping (Iterative DFS)
        # Initialize with root
        self.old2New = {self.root: 0}
        self.new2Old = [self.root] # List is faster for int->obj lookup
        
        stack = [self.root]
        
        # Local variable caching for speed
        P = self.P
        D = self.D
        E = self.E
        old2New = self.old2New
        new2Old = self.new2Old
        
        next_id = 1
        
        while stack:
            u_old = stack.pop()
            u_new = old2New[u_old]
            
            # Iterate over neighbors
            for v_old in E[u_old]:
                if v_old not in old2New:
                    # Assign new integer ID
                    v_new = next_id
                    next_id += 1
                    
                    # Store Mappings
                    old2New[v_old] = v_new
                    new2Old.append(v_old)
                    
                    # Set immediate parent (2^0) and depth
                    P[v_new][0] = u_new
                    D[v_new] = D[u_new] + 1
                    
                    stack.append(v_old)

        # 2. Build Binary Lifting Table
        # Optimization: Loop j outside, i inside. 
        # This is much faster in Python than doing it inside the DFS.
        for j in range(1, self.LOG):
            prev_j = j - 1
            for i in range(self.N):
                # P[i][j] = Parent[ Parent[i][j-1] ][j-1]
                P[i][j] = P[P[i][prev_j]][prev_j]

    def query(self, p, q):
        # Convert external names to internal IDs
        if p not in self.old2New or q not in self.old2New:
            return None # Handle missing nodes gracefully
            
        u = self.old2New[p]
        v = self.old2New[q]
        
        D = self.D
        P = self.P

        # Ensure u is deeper or equal to v
        if D[u] < D[v]:
            u, v = v, u
        
        # 1. Lift u to the same depth as v
        diff = D[u] - D[v]
        for j in range(self.LOG):
            if (diff >> j) & 1:
                u = P[u][j]
        
        if u == v:
            return self.new2Old[u]

        # 2. Lift both nodes until they are just below the LCA
        for j in range(self.LOG - 1, -1, -1):
            if P[u][j] != P[v][j]:
                u = P[u][j]
                v = P[v][j]
        
        # Return the parent of the stopping point
        return self.new2Old[P[u][0]]

N, Q= list(map(int, input().split()))
P = list(map(int, input().split()))
edges = defaultdict(list)

for i, x in enumerate(P):
    edges[x].append(i+1)
lca = LCA(edges, N,0)
lca.process()
for _ in range(Q):
    p, q = list(map(int, input().split()))
    print(lca.query(p,q))
