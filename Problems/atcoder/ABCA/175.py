s = input()
from itertools import groupby

l = [list(v) for k, v in groupby(s)]
mx = 0
for x in l:
    if x[0] == "R": mx = max(mx, len(x))
print(mx)
