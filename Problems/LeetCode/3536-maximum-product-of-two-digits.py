class Solution:
    def maxProduct(self, n: int) -> int:
        n = str(n)
        mx = 0
        for i in range(len(n)-1):
            for j in range(i+1, len(n)):
                mx = max(mx, int(n[i])* int(n[j]))
        return mx