class Solution:
    def specialArray(self, nums: List[int]) -> int:
        count = dict(Counter(nums)).items()
        for i in range(100,-1,-1):
            total = 0
            for k, v in count:
                if k >=i:
                    total += v

            if total == i: return i
        return -1
