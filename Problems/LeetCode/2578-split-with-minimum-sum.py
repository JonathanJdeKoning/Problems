class Solution:
    def splitNum(self, num: int) -> int:
        s = str(num)
        nums = sorted([int(c) for c in s])
        first = ""
        sec = ""
        for i in range(0,len(nums),2):
            first += str(nums[i])
        for i in range(1,len(nums),2):
            sec += str(nums[i])
        return int(first) + int(sec)