class Solution:
    def countTriples(self, n: int) -> int:
        total = 0
        squares = [x*x for x in range(1,n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i**2 + j**2 in squares:
                    total += 1
        return total
