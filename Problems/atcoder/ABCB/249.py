from itertools import pairwise
S = input()

u = [c for c in S if c.isupper()] 
l = [c for c in S if c.islower()]
if not u or not l: exit(print("No"))

if len(set(S)) == len(S):
    print("Yes")
else:
    print("No")