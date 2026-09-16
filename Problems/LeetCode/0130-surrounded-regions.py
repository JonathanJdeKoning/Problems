class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        R, C = len(board), len(board[0])
        s = []
        bad = set()
        for i in range(C):
            if board[0][i] == "O":
                s.append((0,i))
            if board[-1][i] == "O":
                s.append((R-1, i))

        for i in range(R):
            if board[i][0] == "O":
                s.append((i, 0))
            if board[i][C-1] == "O":
                s.append((i, C-1))
        while s:
            y, x = s.pop()

            if (y,x) in bad: continue
            bad.add((y,x))

            for dy, dx in directions:
                newY, newX = dy+y, dx+x

                if min(newY, newX) == -1 or newY==R or newX==C or (newY,newX) in bad or board[newY][newX] != "O": continue
                s.append((newY, newX))

        for i in range(R):
            for j in range(C):
                if (i,j) not in bad:
                    board[i][j] = "X"
            
        