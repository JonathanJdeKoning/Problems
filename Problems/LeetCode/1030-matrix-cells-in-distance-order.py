class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        cells = []

        for i in range(rows):
            for j in range(cols):
                cells.append([i,j])

        cells.sort(key=lambda x: abs(rCenter-x[0])+abs(cCenter-x[1]))
        return cells