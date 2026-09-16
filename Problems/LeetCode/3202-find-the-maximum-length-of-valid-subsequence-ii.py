class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        mx = 0
        from collections import Counter
        nums = [x%k for x in nums]
        poss = sorted(Counter(nums).items(), key=lambda x:x[1], reverse=True)

        for a, (i, iCount) in enumerate(poss):
            for b,(j, jCount) in enumerate(poss[a:]):
                if jCount + iCount < mx: continue
                best = 0
                started = False
                curr = None
                for num in nums:
                    if not started:
                        if num == i or num == j:
                            started = True
                            curr = num
                            best+=1
                    else:
                        if num ==i and curr == j:
                            best += 1
                            curr = i
                        elif num == j and curr == i:
                            best += 1
                            curr = j
                mx = max(mx, best)

        return(mx)


        