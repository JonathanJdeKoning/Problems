class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        ans = 0 
        curr = 0
        for r in requests:
            ans += abs(r - curr)
            curr = r
        return ans