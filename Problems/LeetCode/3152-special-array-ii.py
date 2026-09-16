class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
    
        new = [0]
        curr = 0
        start = nums[0]%2
        for num in nums[1:]:
            if num%2==start:
                curr+=1
            new.append(curr)
            start = num%2
        return [new[s]==new[e] for s, e in queries]        