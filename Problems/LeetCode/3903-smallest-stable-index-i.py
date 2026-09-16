class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        x = list(map(lambda i:max(nums[:i+1]) - min(nums[i:]) <= k, range(len(nums))))
        if True in x:
            return x.index(True)
        return -1