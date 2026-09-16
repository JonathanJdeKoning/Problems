good = set()
for i in range(1, 1001):
    k = len(s:=str(i*i))

    for mask in range(2**k):
        total = 0
        conv = [bool(mask & (2**j)) for j in range(k)]

        g = groupby(zip(s, conv), key=lambda x: x[1])
        for key, val in g:
            total += int("".join([v[0] for v in val]))

        if total == i:
            good.add(i)

class Solution:
    def punishmentNumber(self, n: int) -> int:
        return sum(i**2 for i in range(1, n+1) if i in good)