class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        total = 0
        for key, val in freq.items():
            if val > 2:
                mod = val%2
                if mod == 0:
                    total += 2
                else:
                    total += 1
            else: total += val
        return total