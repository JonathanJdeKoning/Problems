class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        for a,b in invocations:
            edges[a].append(b)
        q = deque([k])
        sus = set()
        while q:
            curr = q.popleft()
            if curr in sus: continue
            sus.add(curr)

            for edge in edges[curr]:
                if edge in sus: continue
                q.append(edge)

        ans = []
        for i in range(n):
            if i in sus: continue
            for edge in edges[i]:
                if edge in sus:
                    return list(range(n))
            ans.append(i)
        return ans

