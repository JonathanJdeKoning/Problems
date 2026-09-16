class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        q = deque(sorted(nums))
        ans = 0

        while q:
            mx = q[-1]
            if mx == q[-2]:
                ans += mx
                q.pop()
                q.pop()
                q.popleft()
            else:
                q.pop()
                ans += q.pop()
                q.popleft()
        return ans

        