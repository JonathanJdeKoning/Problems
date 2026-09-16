class Solution:
    def processStr(self, s: str) -> str:
        res = []

        for c in s:
            if c == "*":
                if res:
                    res.pop()
            elif c == "#":
                res *= 2
            elif c == "%":
                res = res[::-1]
            else:
                res.append(c)
        return "".join(res)