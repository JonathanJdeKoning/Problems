class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        count = nums.count(1)
        nums+= nums

        l = 0
        r = count
        ans = nums[l:r].count(0)
        curr = ans
        while True:
            if r >= len(nums): break

            drop = nums[l]
            if drop == 0:
                curr -= 1
            l+=1
            pick = nums[r]
            if pick == 0:
                curr += 1
            r+=1
            ans = min(ans, curr)

        return ans
