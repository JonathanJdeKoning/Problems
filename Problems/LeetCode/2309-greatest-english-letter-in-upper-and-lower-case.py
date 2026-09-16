class Solution:
    def greatestLetter(self, s: str) -> str:
        mx = 0
        for c in s:
            if c.upper() in s and c.lower() in s:
                mx = max(mx, ord(c.upper()))
        return chr(mx) if mx != 0 else ""
