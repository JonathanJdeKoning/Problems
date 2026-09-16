class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        big = []
        for num in nums:
            for k in num: 
                big.append(k)
        return sorted(list(set([x for x in big if big.count(x) == len(nums)])))