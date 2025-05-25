n = list(map(int, input().split()))

from collections import Counter

freq = Counter(n)
if len(freq) == 1:
    print(n[0])
    exit()
for k,v in freq.items():
    if v == 1:
        print(k)
