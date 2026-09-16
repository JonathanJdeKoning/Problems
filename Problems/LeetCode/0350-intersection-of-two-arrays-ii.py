class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        onecount = dict(Counter(nums1))
        twocount = dict(Counter(nums2))
        
        start = set(nums1).intersection(set(nums2))
        end = []
        for num in start:
            mult = min(onecount[num], twocount[num])
            
            for i in range(mult):
                end.append(num)
        return end