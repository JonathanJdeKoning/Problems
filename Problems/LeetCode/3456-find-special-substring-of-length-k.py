class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        for i in range((len(s)-k)+1):
            sub = s[i:i+k]
            if len(set(list(sub))) != 1: continue
            if i != 0:
                if s[i-1] == sub[0]: continue
            if i+k != len(s):
                if s[i+k] == sub[0]: continue
            return True
        return False