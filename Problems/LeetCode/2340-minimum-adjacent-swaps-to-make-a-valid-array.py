class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        mn = min(nums)
        mnIDX = nums.index(mn)

        mx = max(nums)
        mxIDX = [i for i in range(len(nums)) if nums[i] == mx].pop()

        if mnIDX < mxIDX:
            return mnIDX + (N - mxIDX - 1)
        elif mnIDX > mxIDX:
            return mnIDX + (N - mxIDX - 2) 
        else:
            return 0