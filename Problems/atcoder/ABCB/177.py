S = input()
T = input()
best = len(T)


for i in range(len(S) - len(T) + 1):
    curr = 0
    for j in range(len(T)):
        if S[i+j] != T[j]:
            curr += 1
    best = min(best, curr)
print(best)