class Solution:
    def minTimeToType(self, word: str) -> int:
        total = 0
        def dists(a,b):
            main = abs(ord(a)-ord(b))
            return [main, 26-main]
        prev = "a"
        for c in word:
            total += min(dists(c,prev))
            prev = c
        return total + len(word)