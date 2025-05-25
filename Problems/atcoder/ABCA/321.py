from itertools import pairwise

for a, b in pairwise(input()):
    if int(b) >= int(a): print("No");exit(0)
print("Yes")
