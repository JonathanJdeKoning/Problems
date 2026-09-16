R, C = list(map(int, input().split()))
mat = [list(map(int, input().split())) for _ in range(R)]

mn = mat[0][0]

for row in mat:
    for num in row:
        mn = min(mn, num)

ans = 0
for row in mat:
    for num in row:
        ans += num - mn

print(ans)
