class Solution:
    def isDecomposable(self, s: str) -> bool:
        used = False
        g = groupby(s)

        for k, v in g:
            v = list(v)
            m = len(v) % 3
            if m == 0:
                continue
            elif m == 2:
                if used: return False
                else:
                    used = True
            else:
                return False
        return used