class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        top = "qwertyuiop"
        mid = "asdfghjkl"
        bot = "zxcvbnm"
        out = []
        for word in words:
            t = True
            m = True
            b = True
            for c in word.lower():
                if c not in top: t = False
                if c not in mid: m = False
                if c not in bot: b = False
            if any([t,m,b]): out.append(word)
        return out
