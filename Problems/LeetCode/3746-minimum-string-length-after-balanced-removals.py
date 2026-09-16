class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        a = s.count("a")
        b = s.count("b")
        return abs(a-b)