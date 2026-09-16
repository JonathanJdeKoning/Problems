class Solution:
    def reverseByType(self, s: str) -> str:
        new = []
        l = [c for c in s if c.isalpha()]
        y = [c for c in s if not c.isalpha()]

        for c in s:
            if c.isalpha():
                new.append(l.pop())
            else:
                new.append(y.pop())

        return "".join(new)