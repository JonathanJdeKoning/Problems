class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        distpos = 0
        distneg = 0

        pos = start
        while True:
            if pos == len(nums):
                distpos = 999999
                break
            if nums[pos] == target:
                break
            else:
                pos += 1
                distpos += 1
        neg = start
        while True:
            if neg == -1:
                distneg = 999999
                break
            if nums[neg] == target:
                break
            else:
                neg -= 1
                distneg+=1
        return min(distneg, distpos)