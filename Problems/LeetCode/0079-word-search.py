class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        seen = set()
        def dfs(y,x, searchFor):
            seen.add((y,x))

            if searchFor == len(word):
                return True

            char = word[searchFor]

            for dy, dx in directions:
                ny, nx = y+dy, x+dx

                if min(ny,nx) == -1: continue
                if ny == R or nx == C: continue
                if (ny, nx) in seen: continue
                if board[ny][nx] != char: continue

                if dfs(ny, nx, searchFor+1):
                    return True

            seen.discard((y,x))
            return False

        for i in range(R):
            for j in range(C):
                if board[i][j] == word[0]:
                    if dfs(i,j, 1):
                        return True
        return False

