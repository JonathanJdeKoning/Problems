class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if nums.count(0) == 0: return len(nums) - 1
        g = groupby(nums)
        gg = []
        for k, v in g:
            v = list(v)
            gg.append((k, len(v)))

        ans = 0
        print(gg)
        for i in range(len(gg)):
            k, v = gg[i]
            x = 0
            if k == 1:
                ans = max(ans, v)
                continue
            if v == 1:
                if i > 0:
                    x += gg[i-1][1]
                if i < len(gg) - 1:
                    x += gg[i+1][1]
                ans = max(ans, x)

        return ans