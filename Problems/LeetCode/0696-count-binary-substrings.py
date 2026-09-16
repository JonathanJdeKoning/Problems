class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        total = 0
        groups = [list(v) for k,v in groupby(s)]
        for i, group in enumerate(groups[:-1]):
            total += min(len(group), len(groups[i+1]))
        return total