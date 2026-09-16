W, S = map(int, input().split("-"))

if S == 8:
    S = 1
    W += 1
else:
    S += 1

print(f"{W}-{S}")
