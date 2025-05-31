from itertools import pairwise
N, K = map(int, input().split())
taps = list(map(int, input().split()))
if taps[0] > K:
    exit(print("No"))
for a,b in pairwise(taps):
    if b - a > K:
        exit(print("No"))
print("Yes")