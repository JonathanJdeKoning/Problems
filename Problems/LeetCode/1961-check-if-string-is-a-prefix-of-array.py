class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        out = ""
        for word in words:
            out += word
            if out == s: return True
            if len(out) > len(s): return False
        return False