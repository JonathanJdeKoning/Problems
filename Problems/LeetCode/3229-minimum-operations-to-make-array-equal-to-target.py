class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        return reduce(lambda y,x:(y[0]+min(abs(x-y[1]),abs(x))*((x<0)^(y[1]<x)),x),map(lambda y:y[0]-y[1],zip(nums,target)),(0,0))[0]