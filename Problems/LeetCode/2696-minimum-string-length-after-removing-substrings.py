class Solution:
    def minLength(self, s: str) -> int:
        while True:
            old = s
            s = s.replace("AB", "")
            s = s.replace("CD", "")
            if s ==old: return len(s)