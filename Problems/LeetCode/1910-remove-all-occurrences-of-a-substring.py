class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            idx = s.index(part)
            s = s[:idx] + s[idx+len(part):]
        return s