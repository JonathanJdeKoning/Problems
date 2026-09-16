class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        q= deque([source])
        seen = set()
        graph = defaultdict(list)
        for node in edges:
            graph[node[0]].append(node[1])
            graph[node[1]].append(node[0])
        while q:
            curr= q.popleft()
            if curr in seen: continue
            if curr == destination: return True
            seen.add(curr)
            for d in graph[curr]:
                q.append(d)
        return False