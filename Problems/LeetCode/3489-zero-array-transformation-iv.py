class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        mnDec = {}
        for i, num in enumerate(nums):
            if num == 0: continue
            possDec = set()
            found = False
            for j , (l, r, v) in enumerate(queries):
                if i < l or i > r: continue
                if v == num:
                    mnDec[i] = j
                    break

                for poss in list(possDec):
                    new = poss + v
                    if new == num:
                        mnDec[i] = j
                        found = True
                        break
                    possDec.add(poss + v)
                else:
                    possDec.add(v)

                if found: break
            else:
                return -1
        return 1+ max(list(mnDec.values()), default=-1)
                    
                
                