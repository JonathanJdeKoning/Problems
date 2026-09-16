class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        new = [None]*len(s)
        for i,c in enumerate(s):
            if not c.isalpha():
                new[i] = c
        t = [c for c in s if c.isalpha()]
        t = t[::-1]
        mynext = 0

        for i,pos in enumerate(new):
            if not pos:
                new[i] = t[mynext]
                mynext += 1
        return "".join(new)

