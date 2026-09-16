class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = list(accumulate(nums, initial=0))
        mp = {}

        
        #inclusive
        def listSum(i,j):
            return prefix[j+1] - prefix[i]

        ans = -inf
        found = False
        for i, num in enumerate(nums):
            if num not in mp:
                mp[num] = i
            if prefix[i+1] < prefix[mp[num]+1]:
                mp[num] = i
                
            neg = num - k
            pos = num + k
            if neg in mp:
                found = True
                ans = max(ans, listSum(mp[neg], i))
            if pos in mp:
                found = True
                ans = max(ans, listSum(mp[pos], i))


        if not found: return 0
        return ans