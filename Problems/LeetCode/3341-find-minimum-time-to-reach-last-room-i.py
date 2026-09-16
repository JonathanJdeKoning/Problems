class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        dist = [[float('inf')]*m for _ in range(n)]
        dist[0][0] = 0
        h = [(0,0,0)]
        moves = [(0,1),(0,-1),(1,0),(-1,0)]

        while h:
            t,r,c = heapq.heappop(h)

            if t > dist[r][c]:
                continue
            
            if r == n-1 and c == m-1:
                return t

            for dr,dc in moves:
                nr,nc = r+dr,c+dc
                if 0 <= nr < n and 0 <= nc < m:
                    nt = max(t, moveTime[nr][nc])+1
                    if nt < dist[nr][nc]:
                        dist[nr][nc] = nt
                        heapq.heappush(h,(nt,nr,nc))
        
        return dist[n-1][m-1]