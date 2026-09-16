N = int(input())
S = input()

from itertools import pairwise
from collections import Counter


fq = Counter()
for a,b in pairwise(S):
    fq[a+b] += 1

print(fq.most_common()[0][0])