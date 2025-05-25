n = int(input())
s = []
for _ in range(n):
    s.append(input())

from itertools import pairwise
sick = False
for a,b in pairwise(s):
    if sick: print("No"); exit()
    if a=="sweet" and b=="sweet":
        sick = True

print("Yes")
