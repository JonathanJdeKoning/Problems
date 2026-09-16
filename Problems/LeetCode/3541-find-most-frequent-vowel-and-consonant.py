class Solution:
    def maxFreqSum(self, s: str) -> int:
        vow = set("aeiou")
        v = 0
        c = 0
        for x in "qwertyuiopasdfghjklzxcvbnm":
            if x in vow:
                v = max(v, s.count(x))
            else:
                c = max(c, s.count(x))
        return v + c
