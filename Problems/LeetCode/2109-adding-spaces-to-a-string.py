class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        out = []
        spaces = spaces[::-1]
        curr = spaces.pop()
        for i, c in enumerate(s):
            if i == curr:
                out.append(" ")
                if spaces: curr = spaces.pop()
            out.append(c)
        return("".join(out))
