class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:

        ans = 0
        need = sorted([a-b for a,b in zip(capacity, rocks)])
        for n in need:
            if n <= additionalRocks:
                additionalRocks -= n
                ans+= 1
            else: break
        return ans


    