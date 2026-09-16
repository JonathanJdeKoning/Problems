class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        out =[]
        seen = set()
        for num in nums:
            if num in seen: out.append(num)
            seen.add(num)
        return out