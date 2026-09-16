class Solution:
    def countKeyChanges(self, s: str) -> int:
        prev = s[0].lower()
        count = 0
        s = s.lower()
        for c in s:
            if c != prev:
                count += 1
            prev = c
        return count