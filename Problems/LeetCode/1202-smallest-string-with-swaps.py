class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
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
        dsu = DisjointSetUnion(len(s))
        for a,b in pairs:
            dsu.union(a,b)
        
        d = defaultdict(list)

        for i, c in enumerate(s):
            d[dsu.find(i)].append(c)
        
        for k in d.keys():
            d[k] = sorted(d[k],reverse=True)
        
        out = []
        for i,c in enumerate(s):
            group = dsu.parent[i]
            out.append(d[group][-1])
            d[group].pop()
        return "".join(out)



        

