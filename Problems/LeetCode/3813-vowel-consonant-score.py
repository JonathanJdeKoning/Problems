class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v = sum(1 for c in s if c in "aeiou")
        c = sum(1 for x in s if x not in " aeiou1234567890")

        if c <= 0: return 0
        return floor(v / c)