class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        total = 0
        curr = nums[0]
        run = 1
        for num in nums[1:]:
            if num != curr:
                run += 1
                curr = num
            else:
                curr = num
                total += (run*(run+1))//2
                run = 1
        total += (run*(run+1))//2
        return total

                