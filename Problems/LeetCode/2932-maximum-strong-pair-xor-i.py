class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        strong = []
        for i in nums:
            for j in nums:
                if abs(i-j) <= min(i,j):
                    strong.append((i,j))
        mx = -math.inf
        for pair in strong:
            mx = max(mx, pair[0]^pair[1])
        return mx