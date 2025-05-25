l =list(map(int, input().split()))
from collections import Counter

if sorted(Counter(l).values()) == [2,3]: print("Yes")
else: print("No")


