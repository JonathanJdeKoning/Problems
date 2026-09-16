class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        fw = [[inf]*n for _ in range(n)]
        for i in range(n):
            fw[i][i] = 0
        for s, e, w in edges:
            fw[s][e] = w
            fw[e][s] = w
        

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    ans = min(fw[i][j], fw[i][k] + fw[k][j])
                    if ans > distanceThreshold: ans = inf
                    fw[i][j] = ans
        print(fw)
        mn = inf
        out = 0
        for i, row in enumerate(fw):
            ans = n-row.count(inf)-1
            if ans <= mn:
                mn = ans
                out = i
        return out
