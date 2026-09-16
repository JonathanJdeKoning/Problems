class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1: return [0]
        E = defaultdict(set)
        degree = defaultdict(int)
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            E[u].add(v)
            E[v].add(u)

        while n > 2:
            toDelete = []
            for k,v in degree.items():
                if v == 1:
                    toDelete.append(k)
            for x in toDelete:
                u = E[x].pop()
                E[u].discard(x)
                degree[u] -= 1
                del E[x]
                del degree[x]
                n -= 1
        return list(degree.keys())
