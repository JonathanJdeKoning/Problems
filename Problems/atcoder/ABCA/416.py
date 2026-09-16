N, L, R = map(int, input().split())
S = input()
L -= 1
if S[L:R] == "o"*(R-L):
    print("Yes")
else:
    print("No")
