N = int(input())
S = input()
if len(S)%2 == 1:
    exit(print("No"))


mid = len(S)//2

if S[:mid] == S[mid:]:
    print("Yes")
else:
    print("No")