a,b,c = map(int, input().split())
from collections import Counter

freq = Counter([a,b,c])

for k, v in freq.items():
    if v == 1:
        print(k)
