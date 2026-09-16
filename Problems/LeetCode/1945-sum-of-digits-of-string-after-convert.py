class Solution:
    def getLucky(self, s: str, k: int) -> int:
        new = []
        for c in s:
            new.append(str(ord(c)-96))
        new = "".join(new)

        for i in range(k):
            total = 0
            for c in new:
                total += int(c)
            new = str(total)
        return int(new)