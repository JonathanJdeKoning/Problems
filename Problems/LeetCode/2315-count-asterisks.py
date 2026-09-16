class Solution:
    def countAsterisks(self, s: str) -> int:
        good = True
        total = 0
        for c in s:
            if c == "|":
                good = not good
            elif c == "*":
                if good:
                    total += 1
        return total