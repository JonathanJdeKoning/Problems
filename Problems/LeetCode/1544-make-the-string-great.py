class Solution:
    def makeGood(self, s: str) -> str:
        import string
        
        while True:
            l = len(s)
            for c in string.ascii_lowercase:
                s = s.replace(f"{c}{c.upper()}", "")
                s = s.replace(f"{c.upper()}{c}", "")
            if len(s) == l: return s