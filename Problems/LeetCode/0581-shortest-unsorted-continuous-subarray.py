class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if nums == sorted(nums): return  0
        start = None
        end = None
        for i, (a,b) in enumerate(pairwise(nums)):
            if a>b:
                if start is None:
                    start = i
                    end = i+1
                else:
                    end = i+1
        print(start, end)
        mn = min(nums[start:end+1])
        mx = max(nums[start:end+1])
        print(mn, mx)
        ans = end - start + 1
        for i in range(end+1, len(nums)):
            if nums[i] < mx: ans += 1
            else:
                break
        for i in range(start -1, -1, -1):
            if nums[i] > mn: ans += 1
            else:
                break
        return ans