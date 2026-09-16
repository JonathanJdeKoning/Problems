class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        ans = 0
        mp = defaultdict(list)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                a, b= nums[i], nums[j]
                mp[a*b].append(a)
                mp[a*b].append(b)
        for k, v in mp.items():
            p = len(v)//2
            ans += p*(p-1)*4
        return ans