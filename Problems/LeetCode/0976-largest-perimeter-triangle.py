class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        a =0 
        b = 1
        c = 2
        while True:
            A = nums[a]
            B = nums[b]
            C = nums[c]

            if A+B> C and A+C > B and B+C > A: return A+B+C
            a+=1
            b+=1
            c+=1
            if c == len(nums):
                return 0

            