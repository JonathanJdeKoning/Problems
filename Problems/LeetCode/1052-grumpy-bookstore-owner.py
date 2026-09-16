class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        extra = 0
        max_e = 0
        n = len(grumpy)
        base = 0
        for i in range(n):
            if grumpy[i] == 0:
                base += customers[i]
            elif grumpy[i] == 1:
                extra += customers[i]
            if i >= minutes and grumpy[i-minutes] == 1:
                extra -= customers[i-minutes]
            max_e = max(max_e, extra)
        return base + max_e