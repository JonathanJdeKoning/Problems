class Solution:
    def confusingNumber(self, n: int) -> bool:
        mp = {"0": "0", "1":"1", "6":"9", "8":"8", "9":"6"}

        new = []

        for c in str(n):
            if c not in mp: return False
            new.append(mp[c])
        new = int("".join(new[::-1]))
        return new != n