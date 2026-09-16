class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = list(dict(Counter(word1)).values())
        count2 = list(dict(Counter(word2)).values())
        if len(set(list(word1)) - set(list(word2))) > 0: return False
        return sorted(count1) == sorted(count2)