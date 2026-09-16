class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        N = len(s)
        neededWidth = ceil(N / numRows)
        mat = [[""]*500 for _ in range(numRows)]

        curr = 0
        i, j = 0,0
        down = True
        while curr != len(s):
            c = s[curr]
            mat[i][j] = c
            if down:
                i += 1
            else:
                i -= 1
                j += 1
            if i in [0, numRows-1]: down = not down
            curr += 1
        ans = []
        for row in mat:
            ans.append("".join([x for x in row if x]))
        return "".join(ans)
        
