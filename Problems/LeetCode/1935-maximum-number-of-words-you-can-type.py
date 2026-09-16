class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        total = 0
        for word in text:
            bad = False
            for c in brokenLetters:
                if c in word:
                    bad = True
                    break
            if not bad: total += 1
        return total