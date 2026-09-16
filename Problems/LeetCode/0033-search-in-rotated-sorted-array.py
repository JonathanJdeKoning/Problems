from bisect import bisect_left
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def mn(nums):
            if nums[0] < nums[-1]: return 0
            def good(x):
                return nums[x] < nums[0] 

            low = 0
            high = len(nums)-1

            while low < high:
                mid = (low+high)//2

                if good(mid): high = mid
                else: low = mid+1
            return low
        mindex = mn(nums)

        a = bisect_left(nums, target, lo=0, hi=(mindex-1))
        b = bisect_left(nums, target, lo=mindex, hi=(len(nums)-1))
        if a == len(nums): a-= 1
        if b == len(nums): b -= 1
        if nums[a] == target:
            return a
        elif nums[b] == target:
            return b
        return -1


