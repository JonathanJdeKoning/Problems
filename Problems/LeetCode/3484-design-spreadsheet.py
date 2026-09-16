class Spreadsheet:

    def cellFind(self, cell):
        col = ord(cell[0]) - 65
        row = int(cell[1:])
        return row, col

    def __init__(self, rows: int):
        self.sheet = [[0]*26 for _ in range(rows+1)]

    def setCell(self, cell: str, value: int) -> None:
        r,c = self.cellFind(cell)
        self.sheet[r][c] = value

    def resetCell(self, cell: str) -> None:
        r,c = self.cellFind(cell)
        self.sheet[r][c] = 0       

    def getValue(self, formula: str) -> int:
        idx = formula.index("+")
        cellA = formula[1:idx]
        cellB = formula[idx+1:]
        A, B = None, None
        if cellA.isdigit(): A = int(cellA)
        else:
            r,c  = self.cellFind(cellA) 
            A = self.sheet[r][c]
        if cellB.isdigit(): B = int(cellB)
        else:
            r, c = self.cellFind(cellB)
            B = self.sheet[r][c]

        return A + B



# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)