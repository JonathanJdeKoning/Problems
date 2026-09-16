class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)

        fq = Counter(nums1) + Counter(nums2) + Counter(nums3)

        ans = []
        for k, v in fq.items():
            if v >= 2:
                ans.append(k)
        return ans 