mat = []
for i in range(1,10):
    for j in range(1, 10):
        mat.append(i*j)

N = int(input())
ans = 0
for num in mat:
    if num != N:
        ans += num

print(ans)