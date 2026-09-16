from itertools import permutations

X = input()
ans = int(X)
for p in permutations(X):
    if p[0] == "0": continue
    ans = min(ans, int("".join(p)))
print(ans)