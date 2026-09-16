class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        base = list(words[0])
        for word in words[1:]:
            new = []

            for c in word:
                if c in base:
                    new.append(c)
                    base.remove(c)
            base = new
        return base