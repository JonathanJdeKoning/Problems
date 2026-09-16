S = input()
best = 0
l = 0
while l != len(S):
    if S[l] not in "ACGT":
        l += 1
        continue

    r = l+1
    while r != len(S):
        if S[r] in "ACGT":
            r += 1
            continue
        break

    best = max(best, r-l)
    l += 1
print(best)
        