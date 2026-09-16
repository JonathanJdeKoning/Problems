class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        dirs = [(x,y) for x in [-1,0,1] for y in [-1,0,1] if (x,y) != (0,0)]
        R, C = len(board), len(board[0])
        for i in range(R):
            for j in range(C):
                neighbors = 0
                for dy, dx in dirs:
                    ny, nx = i + dy, j + dx
                    if ny not in range(R): continue
                    if nx not in range(C): continue
                    if board[ny][nx] > 0:
                        neighbors += 1
                if board[i][j] == 1:
                    board[i][j] = 10 + neighbors
                else:
                    board[i][j] = -10 - neighbors
        for row in board:
            print(row)
        for i in range(R):
            for j in range(C):
                cell = board[i][j]
                alive = cell > 0
                neighbors = abs(cell) % 10
                if neighbors == 3:
                    board[i][j] = 1
                    continue
                elif neighbors > 3:
                    board[i][j] = 0
                    continue
                elif neighbors == 2:
                    if alive:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
                    continue
                elif neighbors < 2:
                    board[i][j] = 0
                    continue
                else:
                    print("NW")


        