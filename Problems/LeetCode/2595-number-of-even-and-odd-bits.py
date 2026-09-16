class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        b = bin(n)[2:][::-1]

        ev = 0
        od = 0
        for i, c in enumerate(b):
            if c == "1":
                if i%2 == 0: ev += 1
                else: od += 1
        return[ev, od]
