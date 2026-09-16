class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        N = len(encodedText)
        cols = N // rows
        grid = [[""]*cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                grid[i][j] = encodedText[(i*cols)+j]

        ans = []
        i, j = 0,0
        k = 0 
        while k < cols:
            j = k
            while (i < rows) and (j < cols):
                ans.append(grid[i][j])
                j += 1
                i += 1
            i = 0
            k += 1
        return "".join(ans).rstrip()