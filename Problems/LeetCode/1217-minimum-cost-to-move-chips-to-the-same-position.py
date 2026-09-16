class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        count = dict(Counter(position))
        even = 0
        odd = 0
        tot = len(position)
        for pos, num in count.items():
            if pos%2==0: even += num
            else: odd += num        
        return min(even, odd)
