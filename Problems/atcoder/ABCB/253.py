R, C = list(map(int, input().split()))
y = []
x = []
for i in range(R):
    row = input()
    for j in range(C):
        if row[j] == "o":
            y.append(i)
            x.append(j)

print(abs(x[0]-x[1]) + abs(y[0] - y[1]))