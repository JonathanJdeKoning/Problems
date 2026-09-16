class Solution:
    def minimumSteps(self, s: str) -> int:
        need = 0
        ans = 0
        for i in range(len(s)): 
            if s[i] == "0":
                ans += i-need
                need += 1
        return ans

