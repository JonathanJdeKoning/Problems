from itertools import pairwise
input()
nums = list(map(int, input().split()))
out = [a*b for a,b in pairwise(nums)]
print(" ".join(map(str, out)))
