class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        class DisjointSetUnion:
            def __init__(self, n):
                self.parent = list(range(n))
                self.size = [1] * n
                self.num_sets = n

            def find(self, a):
                acopy = a
                while a != self.parent[a]:
                    a = self.parent[a]
                while acopy != a:
                    self.parent[acopy], acopy = a, self.parent[acopy]
                return a

            def union(self, a, b):
                a, b = self.find(a), self.find(b)
                if a != b:
                    if self.size[a] < self.size[b]:
                        a, b = b, a

                    self.num_sets -= 1
                    self.parent[b] = a
                    self.size[a] += self.size[b]

            def set_size(self, a):
                return self.size[self.find(a)]

            def __len__(self):
                return self.num_sets
        dsu = DisjointSetUnion(len(edges)+1)
        ans = None
        for start, end in edges:
            if dsu.find(start) == dsu.find(end): ans = [start,end]
            dsu.union(start, end)
        return ans

        

