H, W = map(int, input().split())

M = []
for _ in range(H):
    M.append(list(input()))

ans = []
for j in range(W):
    col = [row[j] for row in M]
    ans.append(col.count("#"))
print(" ".join(map(str, ans)))
