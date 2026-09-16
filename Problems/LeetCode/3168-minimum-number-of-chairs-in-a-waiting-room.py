class Solution:
    def minimumChairs(self, s: str) -> int:
        need = 0
        mx = 0
        for c in s:
            if c=="E":
                need += 1
                mx = max(mx, need)
            else:
                need -= 1
        return mx