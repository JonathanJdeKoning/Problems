s = list(input())
from collections import Counter

if len(Counter(s)) == 2:
    print("Yes")
else:
    print("No")

