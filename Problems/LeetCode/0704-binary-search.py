class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bad = -1
        good = len(nums)

        def isGood(i):
            return nums[i] >= target

        while good > bad+1:
            mid = (good + bad)//2

            if isGood(mid):
                good = mid
            else:
                bad = mid

        if good == len(nums): return -1
        if nums[good] == target:
            return good
        return -1
