N = int(input())
S = input()

ans = 0

for i in range(len(S)):
    if S[i] != "x": continue
    if (i == 0 or S[i-1] == "x") and (i == len(S)-1 or S[i+1] == "x"): ans += 1
print(ans)
