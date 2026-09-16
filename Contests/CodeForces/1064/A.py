from collections import Counter
def solve():
    N = int(input())
    S = list(input())
    ans = 0
    for i in range(len(S)-2, -1, -1):
        if S[i] != S[i+1]:
            ans += 1
            S[i] = S[i+1]
    print(ans)


for _ in range(int(input())):
    solve()