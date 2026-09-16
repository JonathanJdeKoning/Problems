class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        m = len(nums2)
        
        out = 0
        for i, num1 in enumerate(nums1):
            for j, num2 in enumerate(nums2):
                if num1%(num2*k)==0:
                    out+=1
        return out