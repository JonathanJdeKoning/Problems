class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        for num in nums1:
            idx = bisect_left(nums2, num)
            try:
                if nums2[idx] == num: return num
            except: pass
        return -1