from copy import copy
class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        pos = nums.count(1)
        neg = nums.count(-1)
        
        allNeg = inf
        allPos = inf

        arr = copy(nums)
        if neg % 2 != 1:
            allPos = 0
            for i in range(len(arr) - 1):
                if arr[i] == -1:
                    allPos += 1
                    arr[i] *= -1
                    neg -= 1
                    if arr[i+1] == -1:
                        neg -= 1
                    else:
                        neg += 1
                    arr[i+1] *= -1
                if neg == 0:
                    break
        if neg != 0:
            allPos = inf
        arr = copy(nums)
        if pos % 2 != 1:
            allNeg = 0
            for i in range(len(arr) - 1):
                if arr[i] == 1:
                    allNeg +=  1
                    arr[i] *= -1
                    pos -= 1
                    if arr[i+1] == 1:
                        pos -= 1
                    else:
                        pos += 1
                    arr[i+1] *= -1
                if pos == 0:
                    break
        if pos != 0:
            allNeg = inf
        print(allNeg, allPos)
        if allNeg == inf and allPos == inf: return False
        ans = min(allNeg, allPos)
        if ans <= k: return True
        return False
                    