class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total = 0
        for c in stones:
            if c in jewels:
                total += 1
        return total