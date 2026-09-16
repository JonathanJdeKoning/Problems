class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) <= 3: return False
        def strictInc(nums):
            if len(nums) == 1: return True
            for i in range(1, len(nums)):
                if nums[i] <= nums[i-1]: return False
            return True

        def strictDec(nums):
            if len(nums) == 1: return True
            for i in range(1, len(nums)):
                if nums[i] >= nums[i-1]: return False
            return True


        for p in range(1, len(nums)-2):
            inc = nums[:p+1]
            if not strictInc(inc): continue
            for q in range(p+1, len(nums)-1):
                dec = nums[p:q+1]
                if not strictDec(dec):
                    continue

                inc2 = nums[q:]
                if not strictInc(inc2):
                    continue
                print(p,q)
                return True
        return False
