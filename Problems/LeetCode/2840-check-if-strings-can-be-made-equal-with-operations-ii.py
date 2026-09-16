class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        a = Counter([x for x in s1[::2]])
        b = Counter([x for x in s2[::2]])

        c = Counter([x for x in s1[1::2]])
        d = Counter([x for x in s2[1::2]])

        return a == b and c == d