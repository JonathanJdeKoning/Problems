class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        before, after = p.split("*")
        if before not in s:
            return False

        return after in s[s.index(before)+len(before):]
        