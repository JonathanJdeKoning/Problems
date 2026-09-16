class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        return [1==len(set([b-a for a,b in pairwise(sorted(nums[i:j+1]))])) for i,j in zip(l,r)]