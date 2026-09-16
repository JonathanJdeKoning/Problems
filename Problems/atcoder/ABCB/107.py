R, C = list(map(int, input().split()))
mat = []
for _ in range(R):
    row = list(input())
    if "#" in row:
        mat.append(row)

bad = set()
for j in range(C):
    col = [row[j] for row in mat]
    if "#" not in col:
        bad.add(j)

for row in mat:
    for j in range(C):
        if j in bad: continue
        print(row[j], end="")
    print()

