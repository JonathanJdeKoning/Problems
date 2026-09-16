class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        aSum = sum(nums1)
        bSum = sum(nums2)
        aZeros = nums1.count(0)
        bZeros = nums2.count(0)

        if not aZeros and not bZeros:
            if aSum != bSum: return -1
        if not aZeros:
            if aSum < bSum + bZeros: return -1
            return aSum
        if not bZeros:
            if bSum < aSum + aZeros: return -1
            return bSum

        return max(aSum + aZeros, bSum + bZeros)