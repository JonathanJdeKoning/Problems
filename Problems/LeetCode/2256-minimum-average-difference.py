class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        pref = 0
        suff = sum(nums)
        best = inf
        bestIDX = 0
        for i in range(len(nums)):
            pref += nums[i]
            suff -= nums[i]
            avg1 = floor(pref / (i+1))
            if i == len(nums) - 1:
                avg2 = 0
            else:
                avg2 = floor(suff / (len(nums) - (i+1)))
            diff = abs(avg1 - avg2 )
            if diff < best:
                best = diff
                bestIDX = i
        return bestIDX
