class Solution:
    def balancedStringSplit(self, s: str) -> int:
        total = 0
        ls = 0
        rs = 0
        for c in s:
            if c == "L":
                ls += 1
            if c=="R":
                rs += 1
            if ls == rs:
                total += 1
                ls = 0
                rs = 0
        return total