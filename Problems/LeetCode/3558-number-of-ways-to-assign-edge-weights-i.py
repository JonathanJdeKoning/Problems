class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        mod = int(1e9)+7
        e = defaultdict(list)
        for u,v in edges:
            e[u].append(v)
            e[v].append(u)
        seen = set()
        q = deque([1])
        steps = -1
        while q:
            steps += 1
            for _ in range(len(q)):
                c = q.popleft()
                if c in seen: continue
                seen.add(c)
                
                for v in e[c]:
                    if v not in seen:
                        q.append(v)
        return 2**(steps-1) % mod