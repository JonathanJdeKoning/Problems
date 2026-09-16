class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True, key=lambda x: abs(x))
        poss1 = 1
        pos = 3
        for num in nums:
            if num > 0 and pos !=0:
                poss1*= num
                pos -= 1
        if pos > 0:
            poss1 = -math.inf
        poss2 = 1
        neg = 2
        pos = 1
        for num in nums:
            if num < 0 and neg != 0:
                poss2 *= num
                neg -=1
            elif num > 0 and pos != 0:
                poss2*= num
                pos -=1
        if pos > 0 or neg > 0:
            poss2 = -math.inf
        nums = sorted(nums)
        last = nums[-1]*nums[-2]*nums[-3]
        return max([poss1, poss2, last])


        