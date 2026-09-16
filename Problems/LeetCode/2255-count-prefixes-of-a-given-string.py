class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        total = 0
        for word in words:
            if s.startswith(word):
                total += 1
        return total