class Solution:
    def clearDigits(self, s: str) -> str:
        out = []
        for c in s:
            if c.isdigit():
                out.pop()
            else:
                out.append(c)
        return "".join(out)