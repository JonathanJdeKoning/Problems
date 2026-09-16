class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        R, C = len(board), len(board[0])

        directions = [(0,1), (0,-1), (1,0), (-1,0)]  
        seen = set()

        for i in range(R):
            for j in range(C):
                if board[i][j] == "." or (i,j) in seen:
                    continue
                
                ans += 1
                dfs = [(i,j)]

                while dfs:
                    cy, cx = dfs.pop()
                    seen.add((cy, cx))

                    for dy, dx in directions:
                        ny, nx = cy+dy, cx+dx

                        if min(ny, nx)==-1 or ny==R or nx==C: continue
                        if board[ny][nx] == "." or (ny,nx) in seen: continue
                        
                        dfs.append((ny, nx))
                
        return ans