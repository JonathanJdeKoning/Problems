class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        xs, os = 0, 0

        for row in board:
            xs += row.count("X")
            os += row.count("O")
        
        xWin, oWin = 0,0
        for row in board:
            if row.count("X") == 3: xWin += 1
            if row.count("O") == 3: oWin += 1

        for i in range(3):
            col = [row[i] for row in board]
            if col.count("X") == 3: xWin += 1
            if col.count("O") == 3: oWin += 1

        if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X": xWin += 1
        if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O": oWin += 1
        if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X": xWin += 1
        if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O": oWin += 1

        if xs != os and xs != os+1: return False
        if xWin and oWin: return False
        if oWin and xs > os: return False
        if xWin and os == xs: return False

        return True