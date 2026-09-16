class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        R, C = len(board), len(board[0])


        i, j = click
        d8 = [(a,b) for a in (-1,0,1) for b in (-1,0,1) if (a,b) != (0,0)]

        seen = set()
        if board[i][j] == "M":
            board[i][j] = "X"
            return board
        elif board[i][j] == "E":
            q = deque([(i, j)])
            while q:
                y, x = q.popleft()
                if (y,x) in seen: continue
                seen.add((y,x))
                mines = 0
                pot = []
                for dy, dx in d8:
                    ny, nx = y+dy, x+dx
                    if ny==R or nx==C or ny==-1 or nx==-1: continue
                    if board[ny][nx] == "M":
                        mines += 1
                        continue
                    if board[ny][nx] == "B": continue
                    if board[ny][nx] == "E":
                        if (ny,nx) not in seen:
                            pot.append((ny, nx))
                if mines == 0:
                    board[y][x] = "B"
                    for p in pot:
                        q.append(p)
                else:
                    board[y][x] = str(mines)
                

        return board
