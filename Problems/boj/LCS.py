
from functools import cache
S = input()
T = input()


LCS = [[""]*len(T) for _ in range(len(S))]

for i in range(len(LCS)):
    for j in range(len(LCS[0])):
        if i == 0:
            a = ""
        else:
            a = LCS[i-1][j]
        if j == 0:
            b = ""
        else:
            b = LCS[i][j-1]
        if i == 0 or j == 0:
            c = ""
        else:
            c = LCS[i-1][j-1]

        if S[i] == T[j]:
            LCS[i][j] = c+S[i]
        else:
            if len(a) > len(b):
                LCS[i][j] = a
            else:
                LCS[i][j] = b

ans = LCS[len(S)-1][len(T)-1]
print(len(ans))