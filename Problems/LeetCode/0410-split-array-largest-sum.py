'''
Given an 
    integer array nums and 
    an integer k
Split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.
    A subarray is a contiguous part of the array.
'''
"""
arrays = 0
currSum = 0
for num in nums:
    if currSum + num <= x:
        currSum += num
    else:
        arrays += 1
        currSum = num
a

"""
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
    
        def maxSplitSumSatisfies(x):
            
            arrays = 1
            currentSum = 0
            
            for num in nums:
                if currentSum + num > x:
                    arrays += 1
                    currentSum = num
                    if arrays > k:
                        return False
                else:
                    currentSum += num
            return arrays <= k # arrays <= k
            
        low = max(nums) #good
        high = sum(nums)+1 #bad
        
        if len(nums) == k:
            return low
        
        while high > low:
            mid = (low + high) // 2
            
            if maxSplitSumSatisfies(mid):
                high = mid
            else:
                low = mid + 1
                
        return low
        
            
            
        
        
        