class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        if len(s) == 0: return True
        curr = s[0]
        for c in t:
            if c == curr:
                idx +=1
                if idx == len(s): return True
                curr = s[idx]
        return False