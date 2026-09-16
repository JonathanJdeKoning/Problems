class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        mn = nums[0]
        mndist = abs(0-mn)
        for num in nums[1:]:
            dist = abs(0-num)
            if dist == mndist:
                mn = max(mn, num)
                mndist = min(dist, mndist)
            elif dist < mndist:
                mn = num
                mndist = dist
        return mn