class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        E = defaultdict(set)

        for u,v in dislikes:
            E[u].add(v)
            E[v].add(u)

        seen = {}
        cc = 1
        for i in range(1,n+1):
            if i in seen: continue
            q = deque([i])
            while q:
                cc = -cc
                for _ in range(len(q)):
                    
                    c = q.popleft()
                    seen[c] = cc
                    for v in E[c]:
                        if v in seen and seen[v] == cc: return False
                        if v not in seen:
                            q.append(v)
        return True
