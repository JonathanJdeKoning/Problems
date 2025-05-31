n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
from itertools import pairwise
for x,y in pairwise(sorted(a+b)):
    if x in a and y in a:
        exit(print("Yes"))
print("No")
