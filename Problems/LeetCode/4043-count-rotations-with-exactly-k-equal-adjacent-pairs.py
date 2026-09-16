class Solution:
    def countRotations(self, s: str, k: int) -> int:
        q = deque(s)
        ans = 0
        for _ in range(len(s)):
            q.rotate(1)
            score = sum(1 if a==b else 0 for a,b in pairwise(q))
            if score == k:
                ans += 1
        return ans
