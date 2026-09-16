class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        mx = -1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j <= i: continue
                slc = nums[i:j+1]
                start = slc[0]
                if slc[1] != start + 1: continue
                two = slc[1]
                good = True
                for k, x in enumerate(slc[2:]):
                    if k%2==0:
                        if x != start:
                            good = False
                            break
                    else:
                        if x != two:
                            good = False
                            break
                if good: mx = max(mx, len(slc))
        return mx
