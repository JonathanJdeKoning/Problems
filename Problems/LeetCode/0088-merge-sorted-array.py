class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        aIDX = m-1
        bIDX = n-1
        write = m+n-1

        while write >= 0:
            if aIDX == -1:
                nums1[write] = nums2[bIDX]
                bIDX -= 1
            elif bIDX == -1:
                nums1[write] = nums1[aIDX]
                aIDX -= 1
            elif nums1[aIDX] > nums2[bIDX]:
                nums1[write] = nums1[aIDX]
                aIDX -= 1
            else:
                nums1[write] = nums2[bIDX]
                bIDX -= 1
            write -= 1
        