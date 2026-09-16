class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        fq = Counter(s)

        A = list(fq.values())
        A.sort(reverse=True)

        ans = 0
        while len(A) > k:
            ans += A.pop()
        return ans