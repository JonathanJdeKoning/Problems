class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canEatInTime(k):
            totalHours = 0
            for pile in piles:
                totalHours += ceil(pile / k)
            return totalHours <= h

        low = 0 # Always Bad
        high = max(piles) # Always Good

        while high > low + 1:
            mid = (high + low) // 2

            if canEatInTime(mid):
                high = mid
            else:
                low = mid


        return high