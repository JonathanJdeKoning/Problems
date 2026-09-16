class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        E = defaultdict(set)
        for u, v in connections:
            E[u].add(v)
            E[v].add(u)

        minTime = {-1:inf}
        time = 0
        bridges = []
        seen = set()
        
        def dfs(n,p):
            nonlocal time
            nonlocal bridges
            nonlocal seen

            minTime[n] = time
            seen.add(n)
            for v in E[n] - seen:
                time += 1
                dfs(v, n)

            vTimes = [minTime[v] for v in E[n] if v != p]
            minTime[n] = min(vTimes, default=minTime[n])

            if minTime[n] > minTime[p]:
                bridges.append([n, p])
            
        dfs(0, -1)
        return bridges
