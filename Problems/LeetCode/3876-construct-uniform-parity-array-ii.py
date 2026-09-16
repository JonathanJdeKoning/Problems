class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if len(set([x%2 for x in nums1])) == 1: return True

        mnO = min([x for x in nums1 if x%2==1])
        for num in nums1:
            if num%2==1: continue
            if num-mnO < 1:
                return False
        return True
