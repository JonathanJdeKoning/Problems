R, C = list(map(int, input().split()))


mat = [list(map(int, input().split())) for _ in range(R)]

new = []

for j in range(C):
    col = [row[j] for row in mat]
    new.append(col)

print("\n".join([" ".join(map(str, row)) for row in new]))

