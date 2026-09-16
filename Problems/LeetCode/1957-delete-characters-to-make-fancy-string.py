class Solution:
    def makeFancyString(self, s: str) -> str:
        return"".join(["".join(x)for x in[list(g)[:2]for k,g in groupby(s)]])