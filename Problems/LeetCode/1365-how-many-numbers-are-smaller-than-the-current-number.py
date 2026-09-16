class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new = []
        for num in nums:
            total = 0
            for newnum in nums:
                if newnum < num:
                    total += 1
            new.append(total)
        return new