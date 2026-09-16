class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(list(Counter(list(Counter(s).values())).values())) == 1