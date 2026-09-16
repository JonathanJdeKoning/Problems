class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = list(zip(*board))
        boxes = []
        for i in [0,3,6]:
            for j in [0,3,6]:
                box = []
                box.extend(board[i][j:j+3])
                box.extend(board[i+1][j:j+3])
                box.extend(board[i+2][j:j+3])
                boxes.append(box)
        
        for row in (board + columns + boxes):
            filtered = [num for num in row if num.isdigit()]
            if len(filtered) != len(set(filtered)): return False
        return True





