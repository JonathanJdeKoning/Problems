from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for key, val in dict(counts).items():
            if val == 1:
                return s.index(key)
        return -1