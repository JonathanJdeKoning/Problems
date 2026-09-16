class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        tot = 0
        for word in words:
            allowed = list(chars)
            good = True
            for c in word:
                if c in allowed:
                    allowed.remove(c)
                else:
                    good = False
                    break
            if good:
                tot += len(word)
        return tot