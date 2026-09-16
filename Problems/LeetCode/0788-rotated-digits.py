class Solution:
    def rotatedDigits(self, n: int) -> int:
        mp = {"2":"5",
            "5":"2",
            "6":"9",
            "9":"6"}
        ans = 0
        for i in range(1, n+1):
            s = str(i)
            if "3" in s or "4" in s or"7" in s: continue

            new="".join([mp.get(c, c) for c in s])
            if new != s:
                ans += 1
        return ans 
        