class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        edges = defaultdict(list)

        for i in range(n-1):
            edges[i].append(i+1)
        for s,e in queries:
            edges[s].append(e)

            q = deque([0])
            steps = -1
            seen = set()
            while q:
                steps += 1
                for _ in range(len(q)):
                    curr = q.popleft()
                    if curr == n-1: 
                        ans.append(steps)
                        break
                    if curr in seen: continue
                    seen.add(curr)

                    for edge in edges[curr]:
                        if edge in seen: continue
                        q.append(edge)
                else:
                    continue
                break
        return ans