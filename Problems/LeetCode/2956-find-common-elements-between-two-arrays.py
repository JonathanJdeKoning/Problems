class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        one = 0
        two = 0
        for x in nums1:
            if x in nums2: one += 1
        for x in nums2:
            if x in nums1: two += 1
        return [one,two]
