X, Y = list(map(int, input().split()))

for i in range(X+1):
    j = X - i

    if j*2 + i*4 == Y:
        exit(print("Yes"))
print("No")