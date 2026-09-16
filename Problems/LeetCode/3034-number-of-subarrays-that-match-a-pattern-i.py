class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        start = 0
        end = len(pattern)+1
        
        
        total = 0
        
        while True:
            slc = nums[start:end]
        
            curr = slc[0]
            res = []
            for pos in slc[1:]:
                if pos > curr:
                    res.append(1)
                elif pos < curr:
                    res.append(-1)
                else:
                    res.append(0)
                curr = pos
            if res == pattern:
                total += 1
            start+=1
            end += 1
            if end == len(nums)+1:
                break
        return total
        