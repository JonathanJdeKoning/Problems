class Solution:
    def minimumPushes(self, word: str) -> int:
        total = 0
        cost = 1
        z = 0
        for v in sorted(Counter(word).values(),reverse=True):
            total += v*cost
            z += 1
            if z==8:
                cost += 1
                z = 0
        return total