class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        total = defaultdict(int)
        for num in nums:
            total[num] += num
        mx = max(total)
        houses = [0] * (mx+2)
        for num in total:
            houses[num] = total[num]
        @cache
        def mxRobUptoAndIncluding(i):
            if i == 0:
                return houses[i]
            if i == 1:
                return max(houses[0], houses[1])

            take = houses[i] + mxRobUptoAndIncluding(i-2)
            skip = mxRobUptoAndIncluding(i-1)
            return max(take, skip)
        return mxRobUptoAndIncluding(mx)