class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def canRepairAllCars(t):
            totalRepairable = 0
            for r in ranks:
                repaired = floor(sqrt((t / r)))
                totalRepairable += repaired

            return totalRepairable >= cars

        low = 0
        high = min(ranks) * cars * cars

        while high > low+1:
            mid = low + (high-low) // 2

            if canRepairAllCars(mid):
                high = mid
            else:
                low = mid
        return high
