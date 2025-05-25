a,b,c = map(int, input().split())
from collections import Counter

freq = Counter([a,b,c])

if len(freq) == 2:
    for k,v in freq.items():
        if v ==1:print(k)
elif len(freq) ==3: print(0)
else:
    print(a)
