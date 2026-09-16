class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        nums = [k for k, g in itertools.groupby(nums)]
        numhills = [x for x in range(1,len(nums)-1) if ((nums[x-1] < nums[x]) and (nums[x+1] <nums[x]))]
        numvalls = [x for x in range(1,len(nums)-1) if ((nums[x-1] > nums[x]) and (nums[x+1] >nums[x]))]
        return len(numhills)+len(numvalls)