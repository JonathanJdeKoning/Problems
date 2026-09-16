class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        count = s.count(c)
        
        return int((count**2)/2 + (count/2))