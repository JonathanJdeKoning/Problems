from itertools import pairwise
s = list(map(int, list(input())))

ans = 0


def shift(n, x):
    return (n - x) % 10

totalShifts = 0
while s:
    curr = s.pop()
    ans += 1

    toz = shift(curr, totalShifts)

    ans += toz
    totalShifts += toz


print(ans)


