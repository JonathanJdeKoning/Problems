class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums = nums[::-1]
        fq = Counter(nums)
        dup = len([x for x in fq.values() if x > 1])
        ops =0
        if dup == 0: return 0
        while True:
            ops += 1
            for _ in range(min(3,len(nums))):
                popped = nums.pop()
                fq[popped] -= 1
                if fq[popped] == 1: dup -= 1
            if dup == 0:
                return ops
        
                