A, B = list(map(int, input().split()))
S = input()
if len(S) != A+ B + 1: exit(print("No"))
if S[A] != '-': exit(print("No"))
for i,c in enumerate(S):
    if i == A: continue
    if not c.isdigit():
        exit(print("No"))
print("Yes")