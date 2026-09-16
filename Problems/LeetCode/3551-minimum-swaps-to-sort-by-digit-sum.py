class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        good = sorted(nums, key=lambda x:(sum(int(c) for c in str(x)), x))
        mp = {n:i for i,n in enumerate(nums)}
        ans = 0
        for i, (a,b) in enumerate(zip(nums, good)):
            if a == b: continue
            j = mp[b]
            nums[j], nums[i] = nums[i], nums[j]
            mp[nums[i]], mp[nums[j]] = mp[nums[j]], mp[nums[i]]
            ans += 1
        return ans


            