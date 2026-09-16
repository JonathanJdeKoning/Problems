from operator import __mul__
class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        for mask in range(1 << len(nums)):
            a = []

            b = []
            for j in range(len(nums)):
                if (mask >> j) & 1:
                    a.append(nums[j])
                else:
                    b.append(nums[j])
            if not a or not b: continue
            if reduce(__mul__, a) == target and reduce(__mul__, b) == target: return True
        return False
                