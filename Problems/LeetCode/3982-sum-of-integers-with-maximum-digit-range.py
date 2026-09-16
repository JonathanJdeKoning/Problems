class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        mp = {}
        for num in nums:
            A = [int(x) for x in str(num)]
            mp[num] = max(A) - min(A)

        mx = max(mp.values())
        ans = 0
        for num in nums:
            if mp[num] == mx:
                ans += num

        return ans