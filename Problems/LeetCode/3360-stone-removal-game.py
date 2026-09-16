class Solution:
    def canAliceWin(self, n: int) -> bool:
        curr = 10
        p = 0
        while True:
            if n >= curr:
                n -= curr
                curr -= 1
                p = abs(p-1)
                if curr == -1: curr = 99
            else:
                return bool(p)
