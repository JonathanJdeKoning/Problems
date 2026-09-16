class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        currCol = 0
        for i in range(len(graph)):
            if i not in color:
                q = deque([i])

                while q:
                    for _ in range(len(q)):
                        curr = q.popleft()

                        if curr in color and color[curr] != currCol: return False
                        color[curr] = currCol

                        for edge in graph[curr]:
                            if edge in color and color[edge] == currCol: return False
                            if edge not in color: q.append(edge)
                    currCol = abs(currCol - 1)
        return True
