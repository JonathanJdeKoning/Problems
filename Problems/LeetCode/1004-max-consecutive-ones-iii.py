class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        r = 1
        ans = 0
        curr = int(nums[l] == 0)
        if k == 0:
            for l, v in groupby(nums):
                if l == 1:
                    ans = max(ans, len(list(v)))
            return ans

        while r < len(nums):
            ans = max(ans, (r-l))
            
            while curr <= k:
                if r == len(nums): break
                if nums[r] == 0:
                    if curr == k: break
                    curr += 1
                r += 1

            ans = max(ans, (r-l))

            while curr == k:
                if nums[l] == 0:
                    curr -= 1
                l += 1

        ans = max(ans, r-l)

        return ans
