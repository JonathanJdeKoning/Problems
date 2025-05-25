from collections import Counter
n = int(input())
a = list(map(int, input().split()))
if len(Counter(a)) == 1:
    print("Yes")
else:
    print("No")
