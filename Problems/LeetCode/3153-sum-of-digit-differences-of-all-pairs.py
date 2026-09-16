class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        nums = [str(num) for num in nums]
        n  = len(nums[0])
        out = 0
        for j in range(n):
            col = [int(x) for x in [i[j] for i in nums]]
            count = dict(Counter(col))
            total = 0
            for k1, v1 in count.items():
                for k2,v2 in count.items():
                    if k1!=k2:
                        total += v1*v2
            out+= total//2
        return out