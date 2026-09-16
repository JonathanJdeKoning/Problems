class Solution:
    def shortestSuperstring(self, s1: str, s2: str) -> str:
        if s1 in s2: return s2
        if s2 in s1: return s1
        poss = []
        for i in range(len(s1)):
            if s2.startswith(s1[i:]):
                poss.append(s1[:i] + s2)
                break

        for i in range(len(s2)):
            if s1.startswith(s2[i:]):
                poss.append(s2[:i] + s1)
                break
        if poss:
            return sorted(poss, key=len)[0]
        else:
            return s1 + s2