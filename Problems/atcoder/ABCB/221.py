S = list(input())
T = list(input())
if S == T: exit(print("Yes"))
for i in range(len(S)-1):
    S[i], S[i+1] = S[i+1], S[i]
    if S == T: exit(print("Yes"))
    S[i], S[i+1] = S[i+1], S[i]

print("No")
