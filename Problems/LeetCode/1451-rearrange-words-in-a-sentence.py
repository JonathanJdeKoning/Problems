class Solution:
    def arrangeWords(self, text: str) -> str:
        s = sorted(text.lower().split(), key=lambda x: len(x))
        s[0] = s[0].title()
        return " ".join(s)
