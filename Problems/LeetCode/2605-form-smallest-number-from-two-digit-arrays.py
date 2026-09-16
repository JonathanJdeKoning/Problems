class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        return min([x for x in nums1 if x in nums2]) if len([x for x in nums1 if x in nums2])>0 else int(str(min(min(nums1),min(nums2)))+str(max(min(nums1),min(nums2))))
