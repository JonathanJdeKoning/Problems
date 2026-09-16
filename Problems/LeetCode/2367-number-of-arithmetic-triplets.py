class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        total = 0
        for num in nums:
            if (num + diff) in nums and (num+diff*2)in nums:
                total += 1
        return total