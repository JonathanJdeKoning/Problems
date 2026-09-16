class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        mx = 0
        for num in gain:
            curr += num
            mx = max(mx, curr)
        return mx