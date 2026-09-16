class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        g = groupby(colors)
        a = 0
        b = 0
        for k, v in g:
            val = len(list(v))
            if k == "A":
                a += max(0, val - 2)
            else:
                b += max(0, val - 2)
        if a <= b: return False
        return True
