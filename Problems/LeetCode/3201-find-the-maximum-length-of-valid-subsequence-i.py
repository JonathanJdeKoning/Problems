class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        a = len([x for x in nums if x%2==0])
        a = max(a, len([x for x in nums if x%2==1]))
        
        b=1
        s = nums[0]
        for num in nums[1:]:
            if num%2 != s%2:
                b+=1
                s = num
        return max(b,a)
                