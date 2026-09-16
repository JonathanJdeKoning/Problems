class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = dict(Counter(arr)).values()
        seen = set()
        for c in count:
            if c in seen: return False
            seen.add(c)
        return True
