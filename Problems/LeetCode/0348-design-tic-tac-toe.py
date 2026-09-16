class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[None]*n for _ in range(n)]

    def checkWin(self):
        for i in range(self.n):
            if len(set(self.board[i])) == 1 and self.board[i][0] is not None:
                return self.board[i][0]
        for j in range(self.n):
            col = [row[j] for row in self.board]
            if len(set(col)) == 1 and col[0] is not None:
                return col[0]

        diag1 = [self.board[i][i] for i in range(self.n)]
        diag2 = [self.board[i][(self.n-1)-i] for i in range(self.n)]

        if len(set(diag1)) == 1 and diag1[0] is not None:
            return diag1[0]

        if len(set(diag2)) == 1 and diag2[0] is not None:
            return diag2[0]
        return 0

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        return self.checkWin()
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)