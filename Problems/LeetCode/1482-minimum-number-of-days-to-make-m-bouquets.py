class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) // k < m: return -1

        def canMakeBouquets(daysWaited):
            hasBloomed = [bloomTime <= daysWaited for bloomTime in bloomDay]
            groups = groupby(hasBloomed)
            totalBouquets = 0
            for groupType, group in groups:
                if not groupType : continue

                group = list(group)
                n = len(group)
                groupBouquets = n // k
                totalBouquets += groupBouquets

            return totalBouquets >= m

        low = 1
        high = max(bloomDay)

        while low < high:
            mid = (low + high) // 2

            if canMakeBouquets(mid):
                high = mid
            else:
                low = mid+1
        return low