class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        l= 0
        r = k-1
        out = []
        timer = 0

        start = nums[l:r+1]

        if k ==1: return nums

        for i, (a,b) in enumerate(pairwise(start)):
            if b != a+1:
                timer = i+1

        if timer:
            out.append(-1)
            timer -=1
        else:
            out.append(start[-1])
                

        while True:
            old = nums[r]
            l += 1
            r += 1

            if r == len(nums):
                return out
            
            if timer: out.append(-1)
    
            new = nums[r]

            if new == old+1:
                if not timer:
                    out.append(new)
                else: timer -=1
            else:
                if not timer:
                    out.append(-1)
                timer = k-2

        return out


            
            