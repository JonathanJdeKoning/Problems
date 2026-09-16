class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        words = s.split()
        used = set()
        if len(pattern) != len(words): return False
        for i, c in enumerate(pattern):
            word = words[i]
            if c in d:
                if d[c] != word:
                    return False
            else:
                d[c] = word
                if word in used: return False
                used.add(word)
        return True