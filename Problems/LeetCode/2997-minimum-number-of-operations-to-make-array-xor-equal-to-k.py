class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        start = nums[0]
        for num in nums[1:]:
            start ^= num
        
        startb = bin(start)[2:]
        kb = bin(k)[2:]
        
        startb = startb.zfill(max(len(startb), len(kb)))

        kb = kb.zfill(max(len(startb), len(kb)))


        print(startb)
        print(kb)
        return len([x for x in range(len(kb)) if startb[x] != kb[x]])