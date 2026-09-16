class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        mn = inf
        nums2.sort()
        for i in range(len(nums1)):
            for j in range(len(nums1)):
                if j<=i: continue
                new = nums1[:]
                new.remove(nums1[i])
                new.remove(nums1[j])
                
                new.sort()
                bad = False
                start = -(new[0] - nums2[0])
                for k in range(1, len(nums2)):
                    if -(new[k] - nums2[k]) != start:
                        bad = True
                        break
                if bad:
                    continue
                mn = min(mn, start)
        return mn
                        
        