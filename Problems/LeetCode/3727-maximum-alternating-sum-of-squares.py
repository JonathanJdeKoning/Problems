class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=abs)
        d = deque(nums)
        ans = 0
        while d:
            ans += d.pop()**2
            if d:
                ans -= d.popleft()**2
        return ans