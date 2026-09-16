class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        i = 0
        j = 2

        while j < len(s1):
            if s1[i] != s2[i] or s1[j] != s2[j]:
                s1[i], s1[j] = s1[j], s1[i]

            i += 1
            j += 1
        return s2 == "".join(s1)