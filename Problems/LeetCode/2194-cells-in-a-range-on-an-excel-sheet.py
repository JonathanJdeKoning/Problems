class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start, end = s.split(":")
        def tochar(n): return chr(n+64)
        def tonum(c): return ord(c)-64

        start = [int(tonum(start[0])), int(start[1])]
        end = [int(tonum(end[0])), int(end[1])]
        ans = []
        for i in range(start[0], end[0]+1):
            for j in range(start[1], end[1]+1):
                s = tochar(i)+str(j)
                ans.append(s)
        return ans
