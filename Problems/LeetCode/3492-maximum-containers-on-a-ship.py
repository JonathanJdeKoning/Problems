class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        cells = n*n
        return min(maxWeight // w, cells)