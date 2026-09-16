class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key = len)
        good = set()
        for word in words:
            if len(word) == 1:
                good.add(word)
                continue
            if word[:-1] in good:
                good.add(word)
        return min(good, key = lambda x: (-len(x), x), default = "")
