class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook = (None, None)
        for i, row in enumerate(board):
            if "R" in row:
                rook = (i, row.index("R"))
        rookrow = board[rook[0]]
        rookcol = [row[rook[1]] for row in board]

        print(f"{rookrow=}")
        print(f"{rookcol=}")
        print(f"{rook[0]=}")
        print(f"{rook[1]=}")

        total = 0
        for c in rookrow[rook[1]+1:]:
            if c == "p":
                total += 1
                break
            if c == "B":
                break
        for i in range(rook[1]-1,-1,-1):
            c = rookrow[i]
            if c == "p":
                total += 1
                break
            if c == "B":
                break
        
        for c in rookcol[rook[0]+1:]:
            if c == "p":
                total += 1
                break
            if c == "B":
                break
        for i in range(rook[0]-1,-1,-1):
            c = rookcol[i]
            if c == "p":
                total += 1
                break
            if c == "B":
                break
        

        print(total)
        return total
        
