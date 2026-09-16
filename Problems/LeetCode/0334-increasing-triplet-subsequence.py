class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = nums[0]
        b = inf
        for num in nums[1:]:
            if num <= a:
                a=num
            elif num <= b:
                b = num
            else: return True
        return False