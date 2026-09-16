class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ids = {obj[0]:idx for idx, obj in enumerate(nums1)}
        for id, val in nums2:
            if id not in ids:
                nums1.append([id, val])
                continue
            nums1[ids[id]][1] += val
        nums1.sort()
        return nums1