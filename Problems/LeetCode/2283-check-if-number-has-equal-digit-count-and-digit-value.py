class Solution:
    def digitCount(self, num: str) -> bool:
        for i, c in enumerate(num):
            if num.count(str(i)) != int(c): return False
        return True