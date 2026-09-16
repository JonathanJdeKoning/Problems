N, K = map(int, input().split())

S = input()

bad = set()

for i, c in enumerate(S):
    if c == ".": continue

    for j in range(max(0, i-K), min(len(S), i+K)+1):
        bad.add(j)
ans = 0
for i, c in enumerate(S):
    if c == "." and i not in bad:
        ans += 1
print(ans)
